# Endpoints
## Overview

## Base URL

## Authentication
All endpoints require authentication via a username and a password.
- Permissions
    - IsAuthenticated: Users must be authenticated.

## Error Responses
Error responses follow standard HTTP status codes. Detailed error messages are provided in the response body.

### 
#### List [GET]
- /
- < info >
- Request Body
- Response
#### Create [POST]
- /
- < info >
- Request Body
- Response
#### Retrieve [GET]
- /{uuid}
- Retrieves details of a specific supplier.
- Parameters
- Response
#### Update [PUT, PATCH]
- /{uuid}
- Updates details of a specific < object >.
- Parameters
    - id (uuid,required): The unique identifier of the < object >.
- Request Body
- Response
#### Delete Supplier [DELETE]
- /{uuid}
- Deletes a specific < object >.
- Parameters
    - id (uuid, required): The unique identifier of the < object >.
- Response