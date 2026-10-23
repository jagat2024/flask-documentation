# Flask Routing

## 1. What is Routing?

Routing in Flask is the process of mapping a URL to a specific Python function. When a user visits a URL, Flask executes the corresponding function and returns a response.

**Example:** When a user visits `/about`, Flask executes the `about()` function.

## 2. Basic Route

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation

- `Flask(__name__)`: Creates a Flask application instance.
- `@app.route('/')`: Maps the root URL `/` to the `home()` function.
- `def home()`: Defines the function that handles the request.
- `return`: Sends the response back to the client.
- `app.run(debug=True)`: Starts the development server with debug mode enabled.

## 3. Multiple Routes

A Flask application can contain multiple routes, each handling a different URL.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page!"

@app.route('/about')
def about():
    return "This is About Page"

@app.route('/projects')
def projects():
    return "My Projects"

@app.route('/contact')
def contact():
    return "Contact Us"

if __name__ == '__main__':
    app.run(debug=True)
```

### URL Mapping

| URL | Function | Response |
|---|---|---|
| `/` | `home()` | Welcome to Home Page! |
| `/about` | `about()` | This is About Page |
| `/projects` | `projects()` | My Projects |
| `/contact` | `contact()` | Contact Us |

**Key Point:** Flask calls the function associated with the requested URL.

## 4. Dynamic Routes

Dynamic routes allow a URL to accept variable values.

```python
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"
```

**Example URL:** `/user/Jagat`

**Output:** `Hello, Jagat!`

### Integer Route Parameter

```python
@app.route('/product/<int:product_id>')
def product(product_id):
    return f"Product ID: {product_id}"
```

**Example URL:** `/product/101`

**Output:** `Product ID: 101`

The `<int:product_id>` converter accepts an integer value.

## 5. HTTP Methods in Routing

Flask routes can handle different HTTP methods, such as GET and POST.

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Login form submitted"

    return "Display Login Page"
```

- **GET:** Retrieves a resource or displays a page.
- **POST:** Sends data to the server, such as login form data.

By default, `@app.route()` accepts GET requests and also supports HEAD and OPTIONS as appropriate.

**Security note:** This example only demonstrates routing. A real login system must validate credentials, hash passwords securely, and use appropriate session protection.

## 6. Route Naming and Best Practices

1. Use meaningful function names, such as `home()`, `about()`, and `show_products()`.
2. Use clear and consistent URL patterns.
3. Avoid duplicate endpoint names.
4. Use dynamic routes when a URL needs to accept variable values.
5. Use the appropriate HTTP method for each operation.
6. Keep debug mode enabled only during local development; do not enable it in production.

## 7. Common Routing Errors

| Error | Possible cause | Solution |
|---|---|---|
| 404 Not Found | URL does not match a registered route | Check the URL path |
| 405 Method Not Allowed | Route does not accept the requested HTTP method | Configure the correct methods |
| Endpoint already exists | Duplicate endpoint/function name | Use unique endpoint names |
| Function returns an invalid response | Unsupported return value | Return a valid response, string, or supported response object |

## 8. How to Run the Application

Save the code in `app.py` and run:

```bash
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

## 9. Quick Revision

- **Routing:** Maps URLs to Python functions.
- **Route decorator:** `@app.route()`.
- **Multiple routes:** Multiple URL-function mappings in one application.
- **Dynamic route:** Accepts variable values in the URL.
- **HTTP methods:** Define how a route handles requests.
- **Response:** The data returned by the route function.

### Practice Tasks

1. Create a `/skills` route that returns your technical skills.
2. Create a `/user/<name>` route that greets a user.
3. Create a `/student/<int:student_id>` route that displays a student ID.
4. Create a `/feedback` route that supports GET and POST requests.

**Official documentation:** https://flask.palletsprojects.com/en/stable/quickstart/#routing
