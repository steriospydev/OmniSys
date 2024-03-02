# Product Endpoints
## Overview
This document outlines the RESTful API endpoints for managing product
related information.

## Base URL
The base URL for all endpoints is /product/.

### Category

#### List Category [GET]
- `/category/`
- Retrieves a list of all categories.
- Response
    - `200 OK`: Returns a list of category objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Category [POST]
- `/category/`
- Creates a new category.
- Request Body
    - category_name (string, required): The name of the category.
- Response
    - `201 Created`: Returns the newly created category object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Category [GET]
- `/category/{uuid}`
- Retrieves details of a specific category.
- Parameters
    - id (uuid, required): The unique identifier of the category.
- Response
    - `200 OK`: Returns the details of the specified category.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified supplier does not exist.

#### Update Category [PUT, PATCH]
- `/category/{uuid}`
- Updates details of a specific category.
- Parameters
    - id (uuid,required): The unique identifier of the category.
- Request Body
    - category_name (string, required): The name of the category.
- Response
    - `200 OK`: Returns the updated details of the category.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified category does not exist.

#### Delete Category [DELETE]
- `/category/{uuid}`
- Deletes a specific category.
- Parameters
    - id (uuid, required): The unique identifier of the category.
- Response
    - `204 No Content`: category successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not 
                        provided or are invalid.
    - `404 Not Found`: The specified category does not exist.

### SubCategory

#### List SubCategories [GET]
- `/sub/`
- Retrieves a list of all subcategories.
- Response
    - `200 OK`: Returns a list of subcategory objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create SubCategory [POST]
- `/sub/`
- Creates a new subcategory.
- Request Body
    - `subcategory_name` (string, required): The name of the subcategory.
    - `category` (uuid, required): The unique identifier of the category.
- Response
    - `201 Created`: Returns the newly created subcategory object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve SubCategory [GET]
- `/sub/{id}/`
- Retrieves details of a specific subcategory.
- Parameters
    - `id` (uuid, required): The unique identifier of the subcategory.
- Response
    - `200 OK`: Returns the details of the specified subcategory.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified subcategory does not exist.

#### Update SubCategory [PUT, PATCH]
- `/sub/{id}/`
- Updates details of a specific subcategory.
- Parameters
    - `id` (uuid, required): The unique identifier of the subcategory.
- Request Body
    - Same as Create SubCategory request body.
- Response
    - `200 OK`: Returns the updated details of the subcategory.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified subcategory does not exist.

#### Delete SubCategory [DELETE]
- `/sub/{id}/`
- Deletes a specific subcategory.
- Parameters
    - `id` (uuid, required): The unique identifier of the subcategory.
- Response
    - `204 No Content`: Subcategory successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified subcategory does not exist.

### Package

#### List Packages [GET]
- `/package/`
- Retrieves a list of all packages.
- Response
    - `200 OK`: Returns a list of package objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Package [POST]
- `/package/`
- Creates a new package.
- Request Body
    - `material` (string, required): The material of the package.
    - `package_unit` (string, required): The measurement unit of the package.
    - `package_quantity` (decimal, required): The quantity of the package.
- Response
    - `201 Created`: Returns the newly created package object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Package [GET]
- `/package/{id}/`
- Retrieves details of a specific package.
- Parameters
    - `id` (uuid, required): The unique identifier of the package.
- Response
    - `200 OK`: Returns the details of the specified package.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified package does not exist.

#### Update Package [PUT, PATCH]
- `/package/{id}/`
- Updates details of a specific package.
- Parameters
    - `id` (uuid, required): The unique identifier of the package.
- Request Body
    - Same as Create Package request body.
- Response
    - `200 OK`: Returns the updated details of the package.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or

### Tax

#### List Taxes [GET]
- `/tax/`
- Retrieves a list of all taxes.
- Response
    - `200 OK`: Returns a list of tax objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Tax [POST]
- `/tax/`
- Creates a new tax.
- Request Body
    - `value` (decimal, required): The value of the tax in percentage.
- Response
    - `201 Created`: Returns the newly created tax object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Tax [GET]
- `/tax/{id}/`
- Retrieves details of a specific tax.
- Parameters
    - `id` (uuid, required): The unique identifier of the tax.
- Response
    - `200 OK`: Returns the details of the specified tax.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified tax does not exist.

#### Update Tax [PUT, PATCH]
- `/tax/{id}/`
- Updates details of a specific tax.
- Parameters
    - `id` (uuid, required): The unique identifier of the tax.
- Request Body
    - Same as Create Tax request body.
- Response
    - `200 OK`: Returns the updated details of the tax.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified tax does not exist.

#### Delete Tax [DELETE]
- `/tax/{id}/`
- Deletes a specific tax.
- Parameters
    - `id` (uuid, required): The unique identifier of the tax.
- Response
    - `204 No Content`: Tax successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified tax does not exist.


### Product

#### List Products [GET]
- `/product/`
- Retrieves a list of all products.
- Response
    - `200 OK`: Returns a list of product objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Product [POST]
- `/product/`
- Creates a new product.
- Request Body
    - `product_name` (string, required): The name of the product.
    - `subcategory` (uuid, required): The unique identifier of the subcategory.
    - `package` (uuid, required): The unique identifier of the package.
    - `tax_rate` (uuid, optional): The unique identifier of the tax rate.
    - `summary` (string, optional): Description of the product.
- Response
    - `201 Created`: Returns the newly created product object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Product [GET]
- `/product/{id}/`
- Retrieves details of a specific product.
- Parameters
    - `id` (uuid, required): The unique identifier of the product.
- Response
    - `200 OK`: Returns the details of the specified product.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified product does not exist.

#### Update Product [PUT, PATCH]
- `/product/{id}/`
- Updates details of a specific product.
- Parameters
    - `id` (uuid, required): The unique identifier of the product.
- Request Body
    - Same as Create Product request body.
- Response
    - `200 OK`: Returns the updated details of the product.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified product does not exist.

#### Delete Product [DELETE]
- `/product/{id}/`
- Deletes a specific product.
- Parameters
    - `id` (uuid, required): The unique identifier of the product.
- Response
    - `204 No Content`: Product successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified product does not exist.


#### [Back to Readme](/Readme.md) 
#### [Back to Entpoints](/docs/Entpoints.md) 