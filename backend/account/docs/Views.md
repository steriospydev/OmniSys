#### Views
##### SignupAPIView
- POST
- [HTTP 201 Created, HTTP 400 Bad Request]
- Details:
    - This class defines an API endpoint for user signup.
    - It inherits from APIView.
    - Contains a post method to handle POST requests.
    - Inside the post method:
        - It initializes a serializer with the received request data.
        - Checks if the serializer is valid.
        - If valid, it saves the data and returns a success response with
            HTTP status 201 (Created).
        - If not valid, it returns an error response with HTTP status 400 (Bad Request) along with serializer errors.

##### LoginAPIView
- POST
- [HTTP 200 OK, HTTP 401 Unauthorized, HTTP 400 Bad Request]
- Details:
    - This class defines an API endpoint for user login.
    - It inherits from APIView.
    - Contains a post method to handle POST requests.
    - Inside the post method:
        - It initializes a serializer with the received request data.
        - Checks if the serializer is valid.
        - If valid, it extracts username and password from serializer's validated data.
        - It authenticates the user using authenticate function.
        - If authentication is successful, it retrieves the token associated with the user and returns it along with a success response with HTTP status 200 (OK).
        - If authentication fails, it returns an error response with HTTP status 401 (Unauthorized) indicating invalid email or password.
        - If serializer is not valid, it returns an error response with HTTP status 400 (Bad Request) along with serializer errors.