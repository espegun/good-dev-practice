# How to jsonschema (for Python)

## The purpose
Schemas in general are metadata used to...
1) To share precisely what data should look 
2) Be able to automatically validate that data is correctly formatted

## How does it work?
Remember that with jsonschema (for Python) it is not handling strings, but json objects *after* `json.load()`. 

## Useful commands
`$ pip install jsonschema` Install from PyPI.<br/>
`$ jsonschema -i sample.json sample.schema` You can also run it from the console.<br/>

See the step-by-step intro linked below for the excellent example which is played with in `schema_validation.py`.

## Useful links
[schema.org](https://schema.org/) Bucketloads of schemas.<br/>
[json-schema.org](https://json-schema.org/) Json schema definition.<br/>
[Step-by-step intro](https://json-schema.org/learn/getting-started-step-by-step.html) How to define schemas.<br/>
[jsonschema - an implementation for Python](https://python-jsonschema.readthedocs.io/en/stable/) How to define and validate schemas with Python.<br/>
[jsonschema at the dataplatform](https://github.com/oslokommune/dataplattform/blob/master/docs/jsonschema.md) For use with the dataplatform.<br/>
