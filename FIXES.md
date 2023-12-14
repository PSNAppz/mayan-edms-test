# Project Troubleshooting Documentation

## Overview
This document outlines the steps taken to resolve issues in mayan-edms project, leading to its successful execution.

## Issues Fixed
The main issues addressed were related to the configuration in `settings/base.py`, specifically corrections in static and media roots, and the proper setting of environment variables for database configuration.

### 1. Correction in Static and Media Roots

#### Issue:
The application was not correctly serving static and media files.

#### Solution:
- **Static Root**: The `STATIC_ROOT` setting in `settings/base.py` was corrected. This is the directory where Django stores static files after running the `collectstatic` command.
  
- **Media Root**: Similarly, the `MEDIA_ROOT` setting was fixed. This setting defines the directory where user-uploaded files are stored.

#### Code Changes:
```python
# settings/base.py

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Media files
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### 2. Database Configuration and Environment Variables

#### Issue:
The database configuration was not set up correctly, causing issues with database connectivity.

#### Solution:
- **Environment Variables**: The environment variables related to database configuration were properly set and configured.
- **Database Settings**: Adjustments were made in `settings/base.py` to correctly utilize these environment variables for database connectivity.

#### Code Changes:
```python
# settings/base.py

if not DATABASES:
    if DATABASE_ENGINE:  # NOQA: F821
        DATABASES = {
            "default": {
                "ENGINE": DATABASE_ENGINE,  # NOQA: F821
                "NAME": DATABASE_NAME,  # NOQA: F821
                "USER": DATABASE_USER,  # NOQA: F821
                "PASSWORD": DATABASE_PASSWORD,  # NOQA: F821
                "HOST": DATABASE_HOST,  # NOQA: F821
                "PORT": DATABASE_PORT,  # NOQA: F821
                "CONN_MAX_AGE": DATABASE_CONN_MAX_AGE,  # NOQA: F821
            }
        }
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": str(Path(BASE_DIR, "db.sqlite3")),  # NOQA: F821
            }
        }
```
### 3. Static Files Storage Configuration

#### Issue:
There were issues related to static files storage, caused by the `STATICFILES_STORAGE` setting.

#### Solution:
- **Commented Out Whitenoise Storage**: The line setting `STATICFILES_STORAGE` to use `whitenoise.storage.CompressedManifestStaticFilesStorage` was causing issues and was therefore commented out.

#### Code Changes:
```python
# settings/base.py

# Commented out the following line to resolve static files storage issues
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

### Additional Fixes and Notes
- **Testing**: After making these changes, the application was thoroughly tested to ensure that all static and media files were being correctly served and that the database connections were functioning as expected.
- **NPM Packages**: All necessary npm packages were installed, and static paths were fixed to ensure proper loading of JavaScript and CSS files.
- **Version Control**: Changes were tracked using version control (e.g., Git) to document the process and allow for easy reversion if needed.
