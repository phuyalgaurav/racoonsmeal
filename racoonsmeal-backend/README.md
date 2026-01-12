# Racoonsmeal Backend
This is the api front for the racoonsmeal app.

## API ENDPOINTS
- `/api/schema/` - API schema
- `/api/docs/` - API documentation (Swagger UI)
- `/api/users/register/` - User registration
  - Method: POST
  - Payload:
    ```json
    {
        "username": "general101",
        "password": "first-first",
        "password2": "first-first",
        "email": "general101@gmail.com",
        "first_name": "Solider",
        "last_name": "General",
        "date_of_birth": "1984-01-12"
    }
  - Response:
    ```json
    {
        "username": "general101",
        "email": "general101@gmail.com",
        "first_name": "Solider",
        "last_name": "General",
        "date_of_birth": "1984-01-12"
    }
- `/api/users/login/` - User Login
  - Method: POST
  - Payload:
    ```json
    {
        "username": "general101",
        "password": "first-first"
    }
    ```
  - Response:
    ```json
    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2ODc5MzU1MSwiaWF0IjoxNzY4MTg4NzUxLCJqdGkiOiI2MzQ0ZGNlY2QyMTg0ODUxYjczYTRjNGE5NDNhZDU3NyIsInVzZXJfaWQiOiIyIn0.LDdhy-e9lqoLpjx1g6h6eWWk04HHgWvz6U21L29QHx8",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxODA0MTg4NzUxLCJpYXQiOjE3NjgxODg3NTEsImp0aSI6ImYxZDZmZDM1Yzk5YzQwZjVhNjZhYTcxYzRhY2UwMmE3IiwidXNlcl9pZCI6IjIifQ.VBlFoURxVR2TW_zbaSU5EjqmYEXTi6tCJb4bvFH6MQw"
    }
- `/api/users/profile/` - User Profile
    - Method: GET, PATCH, PUT, CREATE
    - Payload:
      ```json
      {
        "bio": "I am a software developer.",
        "height_cm": 180,
        "weight_kg": 75,
        "profile_picture": "http://example.com/profile.jpg"
      }
    - Response:
      ```json
        {
            "id": 67,
            "bio": "I Am a Software Developer.",
            "height_cm": 67,
            "weight_kg": 67,
            "profile_picture": "http://example.com/profile.jpg",
            "user": {
                "id": 69,
                "username": "general101",
                "email": "general101@gmail.com",
                "first_name": "Solider",
                "last_name": "General",
                "date_of_birth": "1984-01-12"
            },
            "followers": [
                {
                "id": 87,
                "username": "oliverbearman",
                "email": "oliver101@gmail.com",
                "first_name": "Oliver",
                "last_name": "Bearman",
                "date_of_birth": "2004-01-12"
                }
            ]
        }
- `/api/users/change-password/` - Change Password
  - Method: POST, PATCH
  - Payload:
    ```json
    {
        "old_password": "first-first",
        "new_password": "second-second",
        "new_password2": "second-second"
    }

- `api/users/token/refresh/` - Refresh JWT Token
  - Method: POST
  - Payload:
    ```json
    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc2ODc5MzU1MSwiaWF0IjoxNzY4MTg4NzUxLCJqdGkiOiI2MzQ0ZGNlY2QyMTg0ODUxYjczYTRjNGE5NDNhZDU3NyIsInVzZXJfaWQiOiIyIn0.LDdhy-e9lqoLpjx1g6h6eWWk04HHgWvz6U21L29QHx8"
    }
  - Response:
    ```json
    {
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxODA0MTg4NzUxLCJpYXQiOjE3NjgxODg3NTEsImp0aSI6ImYxZDZmZDM1Yzk5YzQwZjVhNjZhYTcxYzRhY2UwMmE3IiwidXNlcl9pZCI6IjIifQ.VBlFoURxVR2TW_zbaSU5EjqmYEXTi6tCJb4bvFH6MQw"
    }