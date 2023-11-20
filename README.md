# FlaskFilm

FlaskFilm is a web application built with Flask, allowing users to browse through a collection of movies stored in a database. While anonymous users can explore the movie listings, account registration is required for users who want to contribute by writing movie reviews.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Launching the app](#launching-the-app)
- [Preview](#preview)

## Features

- Browse through collection of movies.
- User account system for posting movie reviews.
- Moderator capability to remove selected reviews.

## Requirements

Make sure you have the following dependencies installed before running the application:

- alembic==1.12.0
- blinker==1.6.3
- click==8.1.7
- colorama==0.4.6
- Flask==3.0.0
- Flask-Login==0.6.2
- Flask-Migrate==4.0.5
- Flask-SQLAlchemy==3.1.1
- greenlet==3.0.0
- itsdangerous==2.1.2
- Jinja2==3.1.2
- Mako==1.2.4
- MarkupSafe==2.1.3
- SQLAlchemy==2.0.22
- typing_extensions==4.8.0
- Werkzeug==2.3.7

You can install these requirements using the following command:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LukaszFraczek/FlaskFilm
```

2. Install the project dependencies:
```bash
pip install -r requirements.txt
```

## Launching the app

1. Run the Flask application from FlaskFilm folder:
```bash
flask --app website run
```

2. Open web browser of your choice and visit http://localhost:5000 to access FlaskFilm.

## Preview

1. Movies page
![movies](https://github.com/LukaszFraczek/FlaskFilm/assets/30197518/20bb5a1e-ba69-4ef7-bdcf-05ab3b2d20b1)


2. Movie details page
![example](https://github.com/LukaszFraczek/FlaskFilm/assets/30197518/d52e1e4f-47ee-4b35-af41-b45c8d0aae99)
