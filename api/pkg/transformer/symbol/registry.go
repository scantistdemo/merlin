package symbol

import (
	"fmt"
	"strings"

	"github.com/gojek/merlin/pkg/transformer/jsonpath"
	"github.com/gojek/merlin/pkg/transformer/spec"
	"github.com/gojek/merlin/pkg/transformer/types"
	"github.com/gojek/merlin/pkg/transformer/types/operation"
	"github.com/gojek/merlin/pkg/transformer/types/series"
)

const (
	sourceJSONKey       = "__source_json_key__"
	compiledJSONPathKey = "__compiled_jsonpath_key__"

	rawRequestHeadersKey    = "raw_request_headers"
	modelResponseHeadersKey = "model_response_headers"

	preprocessTracingKey  = "__preprocess_tracing_detail__"
	postprocessTracingKey = "__postprocess_tracing_detail__"
)

// Registry contains all symbol (variable and functions) that can be used for expression evaluation
// All keys within Registry can be used as variable in an expression
// All exported method of Registry is accessible as built-in function
type Registry map[string]interface{}

func NewRegistryWithCompiledJSONPath(compiledJSONPaths *jsonpath.Storage) Registry {
	r := Registry{}
	r[compiledJSONPathKey] = compiledJSONPaths
	r[sourceJSONKey] = types.JSONObjectContainer{}

	return r
}

func NewRegistry() Registry {
	r := Registry{}
	r[compiledJSONPathKey] = jsonpath.NewStorage()
	r[sourceJSONKey] = types.JSONObjectContainer{}

	return r
}

func (sr Registry) SetRawRequestJSON(jsonObj types.JSONObject) {
	sr[sourceJSONKey].(types.JSONObjectContainer)[spec.JsonType_RAW_REQUEST] = jsonObj
}

func (sr Registry) SetModelResponseJSON(jsonObj types.JSONObject) {
	sr[sourceJSONKey].(types.JSONObjectContainer)[spec.JsonType_MODEL_RESPONSE] = jsonObj
}

func (sr Registry) JSONContainer() types.JSONObjectContainer {
	return sr[sourceJSONKey].(types.JSONObjectContainer)
}

func (sr Registry) PreprocessTracingDetail() ([]types.TracingDetail, error) {
	return sr.getTracingDetail(preprocessTracingKey)
}

func (sr Registry) PostprocessTracingDetail() ([]types.TracingDetail, error) {
	return sr.getTracingDetail(postprocessTracingKey)
}

func (sr Registry) getTracingDetail(tracingKey string) ([]types.TracingDetail, error) {
	val := sr[tracingKey]
	tracingDetail, ok := val.([]types.TracingDetail)
	if !ok {
		return nil, fmt.Errorf(`type of tracing detail is not '[]types.TracingDetail', found %T`, val)
	}
	return tracingDetail, nil
}

func (sr Registry) SetPreprocessTracingDetail(vals []types.TracingDetail) {
	sr[preprocessTracingKey] = vals
}

func (sr Registry) SetPostprocessTracingDetail(vals []types.TracingDetail) {
	sr[postprocessTracingKey] = vals
}

func (sr Registry) SetRawRequestHeaders(headers map[string]string) {
	sr[rawRequestHeadersKey] = headers
}

func (sr Registry) SetModelResponseHeaders(headers map[string]string) {
	sr[modelResponseHeadersKey] = headers
}

// evalArg evaluate argument
// the argument can be: values or json path string
// if it's json path string, evalArg will extract the value from json path otherwise it will return as is
func (sr Registry) evalArg(arg interface{}) (interface{}, error) {
	switch val := arg.(type) {
	case string:
		if !strings.HasPrefix(val, jsonpath.Prefix) {
			return arg, nil
		}

		cplJsonPath := sr.getCompiledJSONPath(val)
		if cplJsonPath == nil {
			c, err := jsonpath.Compile(val)
			if err != nil {
				return nil, err
			}
			sr.addCompiledJsonPath(val, c)
			cplJsonPath = c
		}

		return cplJsonPath.LookupFromContainer(sr.jsonObjectContainer())
	case *series.Series:
		return val.GetRecords(), nil
	case *operation.OperationNode:
		res, err := val.Execute()
		if err != nil {
			return nil, err
		}
		return sr.evalArg(res)
	case operation.OperationNode:
		res, err := val.Execute()
		if err != nil {
			return nil, err
		}
		return sr.evalArg(res)
	default:
		return arg, nil
	}
}

func (sr Registry) getCompiledJSONPath(jsonPath string) *jsonpath.Compiled {
	compiledJSONPaths, ok := sr[compiledJSONPathKey].(*jsonpath.Storage)
	if !ok {
		return nil
	}

	return compiledJSONPaths.Get(jsonPath)
}

func (sr Registry) addCompiledJsonPath(jsonPath string, c *jsonpath.Compiled) {
	sr[compiledJSONPathKey].(*jsonpath.Storage).Set(jsonPath, c)
}

func (sr Registry) jsonObjectContainer() types.JSONObjectContainer {
	p, ok := sr[sourceJSONKey]
	if !ok {
		return nil
	}
	return p.(types.JSONObjectContainer)
}
