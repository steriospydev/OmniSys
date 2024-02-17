# Testing Plan for Authentication Views in Django Application

## 1. Introduction
This document outlines the testing plan for the authentication views in our Django application. The authentication views handle user signup and login functionalities.

## 2. Objectives
The primary objectives of testing the authentication views are as follows:
- Ensure that users can successfully sign up with valid credentials.
- Verify that users can log in using correct credentials and receive authentication tokens.
- Confirm that appropriate error messages are returned for invalid input data or authentication failures.
- Test edge cases such as existing users attempting to sign up again and incorrect login attempts.
- Validate that tokens are correctly generated and associated with users upon signup and login.

## 3. Scope
The testing plan will cover the following aspects of the authentication views:
- Testing the SignupAPIView for successful and failed signup attempts.
- Testing the LoginAPIView for successful and failed login attempts.
- Testing edge cases such as attempting to sign up with an existing username.
- Verifying token generation and retrieval upon successful signup and login.

## 5. Test Cases
### SignupAPIView
1. Test case for successful signup:
   - Description: Test if a user can successfully sign up with valid credentials.
   - Steps:
     1. Send a POST request to the signup endpoint with valid username and password.
     2. Verify that the response status code is HTTP 201 Created.

2. Test case for failed signup (invalid input data):
   - Description: Test if appropriate error messages are returned for invalid input data.
   - Steps:
     1. Send a POST request to the signup endpoint with invalid or missing data.
     2. Verify that the response status code is HTTP 400 Bad Request.

3. Test case for failed signup (user already exists):
   - Description: Test if attempting to sign up with an existing username results in a failure.
   - Steps:
     1. Create a user with a specific username in the database.
     2. Send a POST request to the signup endpoint with the same username.
     3. Verify that the response status code is HTTP 400 Bad Request.

### LoginAPIView
1. Test case for successful login:
   - Description: Test if a user can successfully log in with correct credentials.
   - Steps:
     1. Create a user in the database with valid credentials.
     2. Send a POST request to the login endpoint with correct username and password.
     3. Verify that the response status code is HTTP 200 OK and contains a token.

2. Test case for failed login (incorrect password):
   - Description: Test if logging in with an incorrect password fails.
   - Steps:
     1. Create a user in the database with a specific username and password.
     2. Send a POST request to the login endpoint with the correct username and incorrect password.
     3. Verify that the response status code is HTTP 401 Unauthorized.

3. Test case for failed login (user does not exist):
   - Description: Test if logging in with a non-existing username fails.
   - Steps:
     1. Send a POST request to the login endpoint with a username that does not exist in the database.
     2. Verify that the response status code is HTTP 401 Unauthorized.

## 6. Test Data
- Test data will be generated programmatically using Django's testing framework.
- Data for edge cases such as existing users will be created manually as part of test setup.

## 7. Test Execution
- Tests will be executed using Django's testing framework and DRF's test utilities.
- Automated tests will be run before each deployment to ensure the stability of the authentication views.

## 8. Conclusion
This testing plan aims to verify the functionality and reliability of the authentication views in our Django application. By following the outlined test cases and procedures, we can ensure that our authentication system behaves as expected under various scenarios.
