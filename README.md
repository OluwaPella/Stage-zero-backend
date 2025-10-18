# Dynamic Profile API

A Django REST API that provides profile information with random cat facts from Cat Facts API.

## Features
- GET /me endpoint with profile data
- Dynamic cat facts from external API
- ISO 8601 timestamp format
- Comprehensive error handling
- CORS enabled

## Local Development
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`
5. Visit: `http://localhost:8000/me`

## API Endpoint
**GET /me**
Returns:
```json
{
    "status": "success",
        "user": {
                "email": "oolaosebikan350@gmail.com",
                        "name": "Olaosebikan Pelumi",
                                "stack": "Python/Django"
                                    },
                                        "timestamp": "2024-01-18T10:30:45.123456Z",
                                            "fact": "Random cat fact here"
                                            }
