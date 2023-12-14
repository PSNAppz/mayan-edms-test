# Local Setup Documentation 

## Overview
This document provides step-by-step instructions for setting up and running the Django project locally for development purposes.

## Prerequisites
- Python (Version recommended by the project)
- PostgreSQL (or another database if the project specifies)
- Node.js and npm (for managing JavaScript dependencies)

## Setup Steps

### 1. Clone the Project Repository
```bash
git clone https://github.com/PSNAppz/mayan-edms-test
cd mayan-edms-test
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install JavaScript Dependencies
Navigate to the directory containing `package.json` and run:
```bash
npm install
```

### 5. Set Up Environment Variables
Create a `.env` file or export environment variables for database settings and other configurations. Or you can simply skip this to use sqlite database.
```plaintext
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
# Add other necessary environment variables
```

### 6. Initialize the Database
Run the following commands to perform migrations:
```bash
python manage.py migrate
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```
This command collects static files in the `STATIC_ROOT` directory.

### 8. Create a Superuser
To access the admin site, create a superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the superuser.

### 9. Run the Development Server
```bash
python manage.py runserver
```
The project should now be running on `http://127.0.0.1:8000/`.

## Additional Configuration (optional)
- **Whitenoise for Static Files**: Project uses Whitenoise for static file handling in production, ensure it's configured correctly.
- **Additional Services**: The project uses other services (like Redis, Celery), set them up accordingly.
- **Testing**: Run tests to ensure everything is set up correctly.
  ```bash
  python manage.py test
  ```

## Notes
- Always activate the virtual environment (`venv`) before working on the project.
- Keep dependencies updated and regularly pull changes from the repository.
- For production deployment, additional steps and security measures will be required.
