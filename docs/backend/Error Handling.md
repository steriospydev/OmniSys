# Error Handling
The API follows standard HTTP status codes to communicate the result of a request. In case of errors, additional information is provided in the response body.

### Error Response Format

In case of an error, the API returns a JSON object with the following structure:
```  
{
    "error": {
        "code": "error_code",
        "message": "Error message explaining the issue"
        }
}
```

### The API uses the following HTTP status codes to indicate the result of a request:

- 200 OK: The request was successful.
- 201 Created: The resource was successfully created.
- 204 No Content: The request was successful, and there is no content to return.
- 400 Bad Request: The request is invalid or malformed.
    + ```
        {
            "error": {
                "code": "invalid_request",
                "message": "The request is missing required parameters"
            }
        }
        ```
- 401 Unauthorized: Authentication is required to access the resource.
    + ```
        {
            "error": {
                "code": "unauthorized",
                "message": "Authentication credentials are missing or invalid"
                }
        }
        ```     
- 403 Forbidden: The client does not have permission to access the resource.
    + ```
        {
            "error": {
                "code": "forbidden",
                "message": "You do not have permission to access this resource"
                }
        }
    ```
- 404 Not Found: The requested resource does not exist.
    + ```
        {
            "error": {
                "code": "not_found",
                "message": "The requested resource does not exist"
            }
        }
    ```

- 405 Method Not Allowed: The HTTP method used is not allowed for the requested resource.
- 429 Too Many Requests: The client has exceeded the rate limit.
    + ```
        {
            "error": {
                "code": "rate_limit_exceeded",
                "message": "You have exceeded the rate limit for this endpoint"
                }
        }
        ```

- 500 Internal Server Error: An unexpected error occurred on the server.
    + ```
        {
            "error": {
                "code": "internal_server_error",
                "message": "An unexpected error occurred on the server"
            }
        }
        ```


### Handling Errors
- Clients should always check the HTTP status code of the response to determine the outcome of their request.
- If an error occurs, clients can parse the error response body to obtain more information about the error.
- Clients should handle errors gracefully and provide meaningful feedback to users.



#### [Back to Readme.md](/Readme.md) 