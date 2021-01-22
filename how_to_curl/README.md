# How to cURL (client URL)

## The purpose
A tool to transfer data to or from a server, supporting a bunch of protocols. It can be run from the terminal, shell scripts and is often handy when working against APIs.

## How does it work?
...

## Useful commands
`$ curl www.google.com` Get the static content of a page.  
`$ curl -O https://testdomain.com/testfile.tar.gz` (Upper case letter O). Download a file and save it locally *with the same name*.  
`$ curl -o custom_file.tar.gz https://testdomain.com/testfile.tar.gz` (Lower case letter o). Download a file and save it *with the custom name*.  
`$ curl -d "param1=test1&param2=test2" http://test.com` Make a POST request.  
`$ curl -H 'Content-Type: application/json' -d '{"param1":"test1","param2":"test2"}' http://www.test.com` Make a POST request with JSON.  





## Useful links
[10 Curl commands you should know](https://link.medium.com/AfZeGwxVcdb)  **WIP**
