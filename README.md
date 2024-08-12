# DjangoAuthenticationSystem

## Overview

**DjangoAuthenticationSystem** is a project that demonstrates the powerful authentication features provided by Django. This project explores the use of Django’s built-in authentication system, including user registration, login, logout, password reset, and user profile management.

## Features

- **User Registration:** New users can register with a username, email, and password.
- **User Login/Logout:** Secure user login and logout functionality.
- **Password Reset:** Users can reset their passwords via email.
- **User Profile Management:** Users can update their personal information.
- **Session Management:** Secure session management to keep users logged in.

## Prerequisites

- **Python 3.x**
- **Django 3.x or later**
- **MySQL or SQLite** (Default is SQLite)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pedro162/DjangoAuthenticationSystem.git
cd DjangoAuthenticationSystem
```

### 2. Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Update your `settings.py` file with your database credentials. For example, to use MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

Create an admin account to manage users:

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Your application will be available at `http://127.0.0.1:8000/`.

## Screenshots

### User Registration

![User Registration](screenshots/user_registration.png)

### User Login

![User Login](screenshots/user_login.png)

### Password Reset

![Password Reset](screenshots/password_reset.png)

### User Profile

![User Profile](screenshots/user_profile.png)

## How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License
