# Simple Auth Project

This is a simple Django project demonstrating session-based authentication with role-based content.

## Features

- **Login Page**: Accepts specific usernames to determine roles.
- **Home Page**: Displays different text based on the logged-in user:
  - `murali` -> "You're the owner"
  - `yashu` -> "You're the employee"
- **About Page**: Publicly accessible page.
- **Session Management**: Uses Django sessions to persist login state.

## How to Run

1.  Navigate to the project directory:
    ```bash
    cd c:\Users\YOGESH\OneDrive\Desktop\abacus\Backend\day5\prj
    ```

2.  Run the development server:
    ```bash
    python manage.py runserver
    ```

3.  Open your browser and visit:
    - [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Credentials

- **Owner**: `murali`
- **Employee**: `yashu`
