# Flask Query Parameters

## 1. What are Query Parameters?

Query parameters are key-value pairs passed through a URL to send additional information to the server.

They are commonly used for searching, filtering, sorting, and pagination in web applications and APIs.

### Example URL

```text
http://127.0.0.1:5000/search?name=Jagat&city=Kolkata
```

Explanation:

- `/search` is the URL path.
- `?` marks the beginning of the query string.
- `name=Jagat` is the first query parameter.
- `&` separates multiple query parameters.
- `city=Kolkata` is the second query parameter.

## 2. Accessing Query Parameters in Flask

Flask provides `request.args` to access query parameters from an incoming HTTP request.

### Example Code

```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page"

@app.route("/search")
def search():
    name = request.args.get("name")
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation

- `Flask(__name__)` creates the Flask application.
- `@app.route("/search")` defines the search endpoint.
- `request.args.get("name")` retrieves the value of the `name` query parameter.
- `app.run(debug=True)` starts the development server when the file is executed directly.

**Important:** `__name__` is a Python special variable. Do not put quotes around it in the main guard.

## 3. Testing the Application

Start the application:

```bash
python app.py
```

Open the following URLs in your browser.

### Example 1: Home Page

```text
http://127.0.0.1:5000/
```

Output:

```text
This is the home page
```

### Example 2: Query Parameter with a Value

```text
http://127.0.0.1:5000/search?name=Jagat
```

Output:

```text
Hello Jagat
```

### Example 3: Different Query Parameter Value

```text
http://127.0.0.1:5000/search?name=Rahul
```

Output:

```text
Hello Rahul
```

### Example 4: Missing Query Parameter

```text
http://127.0.0.1:5000/search
```

Output:

```text
Hello None
```

The output is `None` because the `name` parameter was not provided and no default value was specified.

## 4. Using Default Values

We can provide a default value using the `get()` method.

```python
@app.route("/search")
def search():
    name = request.args.get("name", "Guest")
    return f"Hello {name}"
```

Request:

```text
http://127.0.0.1:5000/search
```

Output:

```text
Hello Guest
```

## 5. Multiple Query Parameters

Multiple query parameters can be passed using `&`.

Example URL:

```text
http://127.0.0.1:5000/search?name=Jagat&city=Kolkata
```

Code:

```python
@app.route("/search")
def search():
    name = request.args.get("name", "Guest")
    city = request.args.get("city", "Unknown")

    return f"{name} lives in {city}"
```

Output:

```text
Jagat lives in Kolkata
```

## 6. Converting Query Parameters into Integers

Query parameter values are generally returned as strings. Use the `type` argument when an integer is required.

```python
@app.route("/age")
def age():
    user_age = request.args.get("age", default=0, type=int)
    return f"Your age is {user_age}"
```

Request:

```text
http://127.0.0.1:5000/age?age=21
```

Output:

```text
Your age is 21
```

If the parameter is missing or cannot be converted to an integer, this example returns the default value `0`.

## 7. Query Parameters vs URL Path Parameters

| Feature | Query Parameters | URL Path Parameters |
|---|---|---|
| Example | `/search?name=Jagat` | `/users/21` |
| Flask access | `request.args.get("name")` | Function argument |
| Typical purpose | Search, filter, sort | Identify a resource |
| Route example | `@app.route("/search")` | `@app.route("/users/<int:user_id>")` |

### URL Path Parameter Example

```python
@app.route("/users/<int:user_id>")
def get_user(user_id):
    return f"User ID: {user_id}"
```

Request:

```text
http://127.0.0.1:5000/users/21
```

Output:

```text
User ID: 21
```

## 8. Common Use Cases

- **Search:** `/search?query=python`
- **Filtering:** `/products?category=laptop`
- **Sorting:** `/products?sort=price`
- **Pagination:** `/products?page=2&limit=10`
- **User preferences:** `/articles?language=en`

## 9. Best Practices

1. Use `request.args.get()` when a parameter may be missing.
2. Provide sensible default values where appropriate.
3. Validate input types and allowed values.
4. Do not assume that query parameters are trustworthy.
5. Avoid putting passwords, API secrets, or sensitive tokens in URLs.
6. Use `debug=True` only for local development, not production deployment.

## 10. Key Takeaways

- Query parameters send additional information through a URL.
- The `?` begins the query string.
- The `&` separates multiple parameters.
- Flask uses `request.args` to access query parameters.
- `request.args.get("key")` retrieves a value.
- `request.args.get("key", "default")` provides a default value.
- Use `type=int` when integer conversion is required.

## 11. Official Documentation

- Flask API — Request and `request.args`: https://flask.palletsprojects.com/en/stable/api/#flask.Request.args
- Flask Quickstart: https://flask.palletsprojects.com/en/stable/quickstart/

