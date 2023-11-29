# FlaskFilm

FlaskFilm is a web application built with Flask, allowing users to browse through a collection of movies stored in a database. While anonymous users can explore the movie listings, account registration is required for users who want to contribute by writing movie reviews.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Launching the app](#launching-the-app)
- [Preview](#preview)

## Features

- Browse through collection of movies.
- User account system for posting movie reviews.
- Moderator capability to remove selected reviews.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LukaszFraczek/FlaskFilm
cd FlaskFilm
```

2. Set up a Python virtual environment (optional but recommended):
```bash
# On Windows
python -m venv venv

# On macOS and Linux
python3 -m venv venv
```

3. Activate the virtual environment (if set up):
```bash
# On Windows
venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate
```

4. Install the project dependencies:
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
