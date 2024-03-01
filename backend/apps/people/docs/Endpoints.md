# People Endpoints
## Overview
This document outlines the RESTful API endpoints for managing people.

## Base URL
The base URL for all endpoints is /people/.


### Supplier
#### List Suppliers [GET]
- /supplier/
- Retrieves a list of all suppliers.
- Response
    - 200 OK: Returns a list of supplier objects.
    - 401 Unauthorized: Authentication credentials were not provided or are invalid.

#### Create Supplier [POST]
- /supplier/
- Creates a new supplier.
- Request Body
    - company (string, required): The name of the company.
    - tin_num (string, required): 9 digits unique TIN 
    - person (string, optional):
    - tin_agency (string, optional)
    - city (string ,optional)
    - email (string ,optional)
    - area (string ,optional)
    - address (string ,optional)
    - zipcode (string ,optional)
    - phone (string ,optional)
- Response
    - 201 Created: Returns the newly created supplier object.
    - 400 Bad Request: Invalid request body.
    - 401 Unauthorized: Authentication credentials were not provided or are invalid.

#### Retrieve Supplier [GET]
- /supplier/{uuid}
- Retrieves details of a specific supplier.
- Parameters
    - id (uuid, required): The unique identifier of the supplier.
- Response
    - 200 OK: Returns the details of the specified supplier.
    - 401 Unauthorized: Authentication credentials were not provided or are invalid.
    - 404 Not Found: The specified supplier does not exist.

#### Update Supplier [PUT, PATCH]
- /supplier/{uuid}
- Updates details of a specific supplier.
- Parameters
    - id (uuid,required): The unique identifier of the supplier.
- Request Body
    - company (string, required): The name of the company.
    - tin_num (string, required): 9 digits unique TIN 
    - person (string, optional):
    - tin_agency (string, optional)
    - city (string ,optional)
    - email (string ,optional)
    - area (string ,optional)
    - address (string ,optional)
    - zipcode (string ,optional)
    - phone (string ,optional)
- Response
    - 200 OK: Returns the updated details of the supplier.
    - 400 Bad Request: Invalid request body.
    - 401 Unauthorized: Authentication credentials were not provided or are invalid.
    - 404 Not Found: The specified supplier does not exist.

#### Delete Supplier [DELETE]
- /supplier/{uuid}
- Deletes a specific supplier.
- Parameters
    - id (uuid, required): The unique identifier of the supplier.
- Response
    - 204 No Content: Supplier successfully deleted.
    - 401 Unauthorized: Authentication credentials were not 
                        provided or are invalid.
    - 404 Not Found: The specified supplier does not exist.