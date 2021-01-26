# How to cURL (client URL)

## The purpose
A tool to transfer data to or from a server, supporting a bunch of protocols. It can be run from the terminal, shell scripts and is often handy when working against APIs.

## How does it work?

The below is not limited to cURL, but useful to know.

### Reminder: [HTTP methods](https://www.w3schools.com/tags/ref_httpmethods.asp)
- **GET** - To request data from a specified resource.
- **POST** - To send data to create or update a resource.

### Reminder: [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- **200 OK**: The request has succeeded.
- **400 Bad Request**: Invalid syntax in the request.
- **401 Unauthorized**: Unauthorized, the client must autenticate itself.
- **403 Forbidden**: The client is identified, but does not have access.  
- **404 Not Found**: The client was able to communicate with the server, but didn't get the needed response.

## Useful commands
`$ curl www.google.com` Get the static content of a page.  
`$ curl -O https://testdomain.com/testfile.tar.gz` (Upper case letter O). Download a file and save it locally *with the same name*.  
`$ curl -o custom_file.tar.gz https://testdomain.com/testfile.tar.gz` (Lower case letter o). Download a file and save it *with the custom name*.  
`$ curl -d "param1=test1&param2=test2" http://test.com` Make a POST request.  
`$ curl -H 'Content-Type: application/json' -d '{"param1":"test1","param2":"test2"}' http://www.test.com` Make a POST request with JSON.  

## Useful links
[10 Curl commands you should know](https://link.medium.com/AfZeGwxVcdb)  **WIP**
