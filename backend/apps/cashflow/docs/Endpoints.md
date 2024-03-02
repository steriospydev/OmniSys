# Cashflow Endpoints

## Overview

This document outlines the RESTful API endpoints for managing cashflow-related information.

## Base URL

The base URL for all endpoints is `/cashflow/`.

### Payee Label

#### List Payee Labels [GET]

- `/payeelabel/`
- Retrieves a list of all payee labels.
- Response
    - `200 OK`: Returns a list of payee label objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Payee Label [POST]

- `/payeelabel/`
- Creates a new payee label.
- Request Body
    - `name` (string, required): The name of the payee label.
- Response
    - `201 Created`: Returns the newly created payee label object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Payee Label [GET]

- `/payeelabel/{id}/`
- Retrieves details of a specific payee label.
- Parameters
    - `id` (uuid, required): The unique identifier of the payee label.
- Response
    - `200 OK`: Returns the details of the specified payee label.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payee label does not exist.

#### Update Payee Label [PUT, PATCH]

- `/payeelabel/{id}/`
- Updates details of a specific payee label.
- Parameters
    - `id` (uuid, required): The unique identifier of the payee label.
- Request Body
    - `name` (string, required): The name of the payee label.
- Response
    - `200 OK`: Returns the updated details of the payee label.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payee label does not exist.

#### Delete Payee Label [DELETE]

- `/payeelabel/{id}/`
- Deletes a specific payee label.
- Parameters
    - `id` (uuid, required): The unique identifier of the payee label.
- Response
    - `204 No Content`: Payee label successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payee label does not exist.

### Payee

#### List Payees [GET]

- `/payee/`
- Retrieves a list of all payees.
- Response
    - `200 OK`: Returns a list of payee objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Payee [POST]

- `/payee/`
- Creates a new payee.
- Request Body
    - `label` (uuid, required): The unique identifier of the payee label.
    - `name` (string, required): The name of the payee.
    - `summary` (string, optional): Summary or description of the payee.
    - `active` (boolean, optional): Indicates whether the payee is active.
- Response
    - `201 Created`: Returns the newly created payee object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Payee [GET]

- `/payee/{id}/`
- Retrieves details of a specific payee.
- Parameters
    - `id` (uuid, required): The unique identifier of the payee.
- Response
    - `200 OK`: Returns the details of the specified payee.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payee does not exist.

#### Update Payee [PUT, PATCH]

- `/payee/{id}/`
- Updates details of a specific payee.
- Parameters
    - `id` (uuid, required): The unique identifier of the payee.
- Request Body
    - Same as Create Payee request body.
- Response
    - `200 OK`: Returns the updated details of the payee.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payee does not exist.

#### Delete Payee [DELETE]

- `/payee/{id}/`
- Deletes a specific payee.
- Parameters
    - `id` (uuid, required): The unique identifier of the payee.
- Response
    - `204 No Content`: Payee successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payee does not exist.

### Payment

#### List Payments [GET]

- `/payment/`
- Retrieves a list of all payments.
- Response
    - `200 OK`: Returns a list of payment objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Payment [POST]

- `/payment/`
- Creates a new payment.
- Request Body
    - `payee` (uuid, required): The unique identifier of the payee.
    - `amount` (decimal, required): The amount of the payment.
    - `summary` (string, optional): Summary or description of the payment.
    - `payment_day` (datetime, optional): The date and time of the payment.
    - `paid` (boolean, optional): Indicates whether the payment is paid.
- Response
    - `201 Created`: Returns the newly created payment object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Payment [GET]

- `/payment/{id}/`
- Retrieves details of a specific payment.
- Parameters
    - `id` (uuid, required): The unique identifier of the payment.
- Response
    - `200 OK`: Returns the details of the specified payment.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payment does not exist.

#### Update Payment [PUT, PATCH]

- `/payment/{id}/`
- Updates details of a specific payment.
- Parameters
    - `id` (uuid, required): The unique identifier of the payment.
- Request Body
    - Same as Create Payment request body.
- Response
    - `200 OK`: Returns the updated details of the payment.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payment does not exist.

#### Delete Payment [DELETE]

- `/payment/{id}/`
- Deletes a specific payment.
- Parameters
    - `id` (uuid, required): The unique identifier of the payment.
- Response
    - `204 No Content`: Payment successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified payment does not exist.

### Source

#### List Sources [GET]

- `/source/`
- Retrieves a list of all sources.
- Response
    - `200 OK`: Returns a list of source objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Source [POST]

- `/source/`
- Creates a new source.
- Request Body
    - `source` (string, required): The source name.
    - `summary` (string, optional): Summary or description of the source.
- Response
    - `201 Created`: Returns the newly created source object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Source [GET]

- `/source/{id}/`
- Retrieves details of a specific source.
- Parameters
    - `id` (uuid, required): The unique identifier of the source.
- Response
    - `200 OK`: Returns the details of the specified source.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified source does not exist.

#### Update Source [PUT, PATCH]

- `/source/{id}/`
- Updates details of a specific source.
- Parameters
    - `id` (uuid, required): The unique identifier of the source.
- Request Body
    - Same as Create Source request body.
- Response
    - `200 OK`: Returns the updated details of the source.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified source does not exist.

#### Delete Source [DELETE]

- `/source/{id}/`
- Deletes a specific source.
- Parameters
    - `id` (uuid, required): The unique identifier of the source.
- Response
    - `204 No Content`: Source successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified source does not exist.

### Income

#### List Incomes [GET]

- `/income/`
- Retrieves a list of all incomes.
- Response
    - `200 OK`: Returns a list of income objects.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Create Income [POST]

- `/income/`
- Creates a new income.
- Request Body
    - `source` (uuid, required): The unique identifier of the income source.
    - `amount` (decimal, required): The amount of the income.
    - `summary` (string, optional): Summary or description of the income.
    - `income_date` (datetime, optional): The date and time of the income.
- Response
    - `201 Created`: Returns the newly created income object.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.

#### Retrieve Income [GET]

- `/income/{id}/`
- Retrieves details of a specific income.
- Parameters
    - `id` (uuid, required): The unique identifier of the income.
- Response
    - `200 OK`: Returns the details of the specified income.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified income does not exist.

#### Update Income [PUT, PATCH]

- `/income/{id}/`
- Updates details of a specific income.
- Parameters
    - `id` (uuid, required): The unique identifier of the income.
- Request Body
    - Same as Create Income request body.
- Response
    - `200 OK`: Returns the updated details of the income.
    - `400 Bad Request`: Invalid request body.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified income does not exist.

#### Delete Income [DELETE]

- `/income/{id}/`
- Deletes a specific income.
- Parameters
    - `id` (uuid, required): The unique identifier of the income.
- Response
    - `204 No Content`: Income successfully deleted.
    - `401 Unauthorized`: Authentication credentials were not provided or are invalid.
    - `404 Not Found`: The specified income does not exist.



#### [Back to Readme](/Readme.md) 
#### [Back to Entpoints](/docs/Entpoints.md) 