# Installation

## Backend

1. Navigate to the backend directory.

2. Create a virtual environment (optional but recommended):
    ```
    python3 -m venv venv
    ```

   This command will create a virtual environment named `venv` in the backend directory.

3. Activate the virtual environment:
    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On Unix or MacOS:
      ```
      source venv/bin/activate
      ```

4. Install the project dependencies by running:
    ```
    pip install -r requirements.txt
    ```

   This command will install all the required Python packages listed in the `requirements.txt` file into the virtual environment.

5. Apply database migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

   This will create the necessary database migrations based on the Django models and apply them to the database.

6. Run tests with coverage:
    ```
    coverage run --source='.' --omit='*/tests/*' manage.py test apps
    ```

   - `--source='.'` tells coverage.py to measure coverage for all files in the current directory.
   - `--omit='*/tests/*'` excludes any files in a `tests` directory from coverage measurement.
   - `manage.py test apps` is the command to run Django tests for the `apps` app (replace `apps` with your app name).

7. After running the tests, you can generate a coverage report:

   - For a textual report, use:
     ```
     coverage report
     ```

   - For a detailed HTML report (recommended for better visualization), use:
     ```
     coverage html
     ```

   The HTML report will be generated in the `htmlcov` directory. You can open `htmlcov/index.html` in your browser to view the coverage details.

## Database

## Frontend


#### [Back to Readme.md](/Readme.md) 