# How to Serverless framework

## The purpose
Useful to build applications of AWS lambdas. It can also be deploy to other *function as a services* such as Azure Functions or Google Cloud Functions. Can be a couple of lambdas or hundreds.

## How does it work?
Hello world with AWS and Python, as described [here](https://www.serverless.com/framework/docs/providers/aws/examples/hello-world/python/). Based on an available template for `serverless.yml` and `handler.py`. 
`sls create --template aws-python3 --path HelloWorld`
Now modify some of the settings in `serverless.yml`:  
...

## Useful commands
`$ sls` Start serverless  
`$ sls upgrade` Upgrade  
`$ sls uninstall` Uninstall


## Useful links
[Getting started and installing](https://www.serverless.com/framework/docs/getting-started/)  
[Getting started with AWS](https://www.serverless.com/framework/docs/providers/aws/)  
[Documentation](https://www.serverless.com/framework/docs/)  
