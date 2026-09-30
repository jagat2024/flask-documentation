# Flask Notes 🚀

> My practical notes for learning Flask with Python.

---

## 1. What is Flask?

Flask is a lightweight Python web framework used to build web applications and APIs.

It is simple, flexible, and easy to get started with.

---

## 2. Why Flask?

Flask is useful for building:

* Web applications
* REST APIs
* Backend services
* Small and medium-sized applications
* Prototypes

---

## 3. Prerequisites

Before learning Flask, you should have basic knowledge of:

* Python
* Functions
* Modules and packages
* HTML
* Basic CSS
* Basic HTTP concepts

---

## 4. Installation

Create a virtual environment:

```bash
python -m venv env
```

Activate it on Windows:

```bash
env\Scripts\activate
```

Install Flask:

```bash
pip install flask
```

Check the installed version:

```bash
flask --version
```

---

## 5. First Flask Application

Create a file named `app.py`:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

Run the application:

```bash
python app.py
```

---

## 6. Understanding the Code

### `from flask import Flask`

Imports the `Flask` class.

### `app = Flask(__name__)`

Creates the Flask application object.

### `@app.route("/")`

Maps the `/` URL to the `home()` function.

### `def home()`

This function runs when the user visits `/`.

### `app.run(debug=True)`

Starts the Flask development server.

`debug=True` helps during development by providing automatic reloading and useful error information.

---

## 7. Project Structure

A basic Flask project can look like this:

```text
project/
│
├── app.py
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    └── js/
```

### `app.py`

Contains the Flask application and routes.

### `templates/`

Contains HTML templates.

### `static/`

Contains CSS, JavaScript, images, and other static files.

---

## 8. Important Flask Concepts

The main concepts I will cover:

* Routing
* Templates
* Jinja2
* Static files
* Forms
* Request and Response
* Sessions
* Cookies
* Databases
* SQLAlchemy
* CRUD
* Authentication
* REST APIs
* Error Handling
* Deployment

---

## 9. Learning Progress

* [x] Flask installation
* [x] First Flask application
* [x] Basic routing
* [ ] Templates
* [ ] Jinja2
* [ ] Static files
* [ ] Forms
* [ ] Database
* [ ] SQLAlchemy
* [ ] CRUD
* [ ] Authentication
* [ ] REST API
* [ ] Deployment

---

## 10. Practice

1. Create a `/` route.
2. Create an `/about` route.
3. Create a `/contact` route.
4. Return HTML from a route.
5. Create a dynamic route using `<username>`.

---

## 📌 Notes

These notes are created while learning Flask through practical examples and projects.

**Learning approach:** Learn → Practice → Build → Document 🚀
