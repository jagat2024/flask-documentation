# Flask URL Converters

## 1. What is a URL Converter?

A URL converter in Flask specifies the type of value that a dynamic URL parameter can accept.

It helps Flask match URLs with the expected data type and pass the converted value to the route function.

**Syntax:**

```python
@app.route('/path/<converter:variable_name>')
```

## 2. Types of URL Converters

| Converter | Description | Example URL |
|---|---|---|
| `string` | Accepts text without `/`. This is the default. | `/user/Jagat` |
| `int` | Accepts a positive or negative integer. | `/student/101` |
| `float` | Accepts a floating-point number. | `/price/99.5` |
| `path` | Accepts text including `/`. | `/files/docs/notes.txt` |
| `uuid` | Accepts a valid UUID value. | `/item/123e4567-e89b-12d3-a456-426614174000` |
| `any` | Accepts one of the specified values. | `/category/books` |

## 3. Examples

### Example 1: String Converter

```python
@app.route('/user/<string:name>')
def user(name):
    return f"Hello, {name}!"
```

**URL:** `/user/Jagat`

**Output:** `Hello, Jagat!`

Note: `string` is the default converter, so `<name>` also works.

### Example 2: Integer Converter

```python
@app.route('/student/<int:student_id>')
def student(student_id):
    return f"Student ID: {student_id}"
```

**URL:** `/student/101`

**Output:** `Student ID: 101`

Flask converts the URL value into a Python integer.

### Example 3: Float Converter

```python
@app.route('/price/<float:amount>')
def price(amount):
    return f"Price: {amount}"
```

**URL:** `/price/99.5`

**Output:** `Price: 99.5`

The value is passed to the function as a Python float.

### Example 4: Path Converter

```python
@app.route('/files/<path:filename>')
def files(filename):
    return f"File path: {filename}"
```

**URL:** `/files/docs/notes.txt`

**Output:** `File path: docs/notes.txt`

Unlike the `string` converter, the `path` converter can accept forward slashes inside the value.

### Example 5: Any Converter

```python
@app.route('/category/<any(books,movies,games):item>')
def category(item):
    return f"Selected category: {item}"
```

**URL:** `/category/books`

**Output:** `Selected category: books`

Only the specified values—`books`, `movies`, or `games`—match this route.

## 4. Why Are URL Converters Useful?

- They validate the expected URL parameter format during route matching.
- They automatically convert values into appropriate Python data types.
- They make dynamic routes easier to understand and maintain.
- They help Flask distinguish between different URL patterns.

**Important:** A converter controls URL matching; it does not replace application-level validation or authorization.

## 5. Quick Revision

- `string` → text
- `int` → integer
- `float` → decimal number
- `path` → text that may contain `/`
- `uuid` → UUID-formatted identifier
- `any` → one of the specified choices

Official documentation: https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules
