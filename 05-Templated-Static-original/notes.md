# Flask Templates and Static Files

## 1. Introduction

Flask applications use templates to generate dynamic HTML pages and static files to serve assets such as CSS, JavaScript, images, and fonts.

### Templates
Templates define the structure and content of web pages. Flask uses the Jinja template engine to render HTML dynamically.

### Static Files
Static files are assets that usually remain unchanged while being served, such as:

- CSS files for styling
- JavaScript files for client-side interactions
- Images and icons
- Fonts and other frontend assets

---

## 2. Templates in Flask

### What is a Template?

A template is an HTML file that can contain dynamic values and control statements.

Instead of writing HTML directly inside a Python function, we create a separate HTML file inside the `templates` directory.

### Project Structure

```text
Flask/
├── app.py
└── templates/
    ├── index.html
    └── about.html
```

### Example 1: Creating a Template

**app.py**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome to Flask</h1>
    <p>This page is rendered using a template.</p>
</body>
</html>
```

### Explanation

- `render_template()` renders an HTML template and returns the resulting response.
- `"index.html"` is the template filename.
- Flask looks for templates inside the `templates` directory by default.

### Expected Output

When you visit `http://127.0.0.1:5000/`, the browser displays:

**Welcome to Flask**

This page is rendered using a template.

---

## 3. Passing Data to Templates

Flask allows us to pass Python variables to templates using keyword arguments in `render_template()`.

### Example

**app.py**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html",
        name="Jagat",
        course="Engineering"
    )

if __name__ == "__main__":
    app.run(debug=True)
```

**templates/index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dynamic Template</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <p>Course: {{ course }}</p>
</body>
</html>
```

### Output

```text
Hello, Jagat!
Course: Engineering
```

### Important Syntax

- `{{ variable }}` displays a value.
- `{% ... %}` executes template logic, such as conditions and loops.
- `{# ... #}` creates a Jinja comment.

---

## 4. Using Conditions and Loops in Templates

Jinja supports conditional statements and loops.

### Example: Conditional Statement

**app.py**

```python
@app.route("/result")
def result():
    marks = 85
    return render_template("result.html", marks=marks)
```

**templates/result.html**

```html
<h1>Exam Result</h1>

{% if marks >= 40 %}
    <p>You passed!</p>
{% else %}
    <p>You failed.</p>
{% endif %}
```

Output:

```text
Exam Result
You passed!
```

### Example: Loop

**app.py**

```python
@app.route("/courses")
def courses():
    course_list = ["Python", "Flask", "Machine Learning"]
    return render_template("courses.html", courses=course_list)
```

**templates/courses.html**

```html
<h1>Available Courses</h1>

<ul>
    {% for course in courses %}
        <li>{{ course }}</li>
    {% endfor %}
</ul>
```

The browser displays an unordered list containing Python, Flask, and Machine Learning.

---

## 5. Static Files in Flask

### What are Static Files?

Static files are frontend assets served separately from the HTML template.

Flask looks for these files in the `static` directory by default.

### Project Structure

```text
Flask/
├── app.py
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
        └── logo.png
```

### Example: Adding CSS

**static/css/style.css**

```css
body {
    background-color: #f0f4f8;
    font-family: Arial, sans-serif;
    text-align: center;
}

h1 {
    color: #2563eb;
}
```

**templates/index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Static Files</title>

    <link
        rel="stylesheet"
        href="{{ url_for('static', filename='css/style.css') }}"
    >
</head>
<body>
    <h1>Welcome to Flask</h1>
    <p>This page uses an external CSS file.</p>
</body>
</html>
```

### Explanation

`url_for('static', filename='css/style.css')` generates the URL for the CSS file.

By default, that URL is:

```text
/static/css/style.css
```

Using `url_for()` is preferable to hardcoding the URL because it works correctly with Flask's configured static URL path.

---

## 6. Linking JavaScript and Images

### JavaScript

Create `static/js/script.js`:

```javascript
console.log("Flask static JavaScript loaded!");
```

Add this to the HTML template:

```html
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

### Images

Place an image at `static/images/logo.png`, then use:

```html
<img
    src="{{ url_for('static', filename='images/logo.png') }}"
    alt="Website logo"
    width="150"
>
```

Flask generates the appropriate URL for each asset.

---

## 7. Templates vs Static Files

| Feature | Templates | Static Files |
|---|---|---|
| Purpose | Generate dynamic HTML | Serve frontend assets |
| Default directory | `templates/` | `static/` |
| Main examples | HTML with Jinja | CSS, JS, images |
| Flask function | `render_template()` | `url_for('static', ...)` |
| Dynamic data | Can receive Python variables | Usually served as-is |

**Remember:** A template can be dynamic, while a CSS file is normally a static asset.

---

## 8. Template Inheritance

Template inheritance helps avoid repeating the same HTML structure across multiple pages.

For example, a website may have a common navigation bar and footer.

### Project Structure

```text
templates/
├── base.html
├── home.html
└── about.html
```

**templates/base.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Flask App{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{{ url_for('home') }}">Home</a>
        <a href="{{ url_for('about') }}">About</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
```

**templates/home.html**

```html
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h1>Welcome Home!</h1>
    <p>This page inherits the base layout.</p>
{% endblock %}
```

**app.py**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
```

The `about.html` template can extend `base.html` in the same way.

### Key Concepts

- `{% extends "base.html" %}` inherits the parent template.
- `{% block title %}` defines a section that child templates can override.
- `{% block content %}` defines the page's main content area.

---

## 9. Common Errors and Fixes

### TemplateNotFound

**Cause:** The template file is missing or stored in the wrong directory.

**Fix:** Verify that the HTML file is inside the `templates` directory and that its filename matches the one passed to `render_template()`.

### CSS Is Not Loading

**Cause:** Incorrect file path or filename.

**Fix:** Check the folder structure and use:

```html
<link
    rel="stylesheet"
    href="{{ url_for('static', filename='css/style.css') }}"
>
```

### JavaScript Is Not Working

**Cause:** Incorrect script path or a JavaScript error.

**Fix:** Verify the file location and check the browser's Developer Tools Console and Network tabs.

### Changes Are Not Visible

**Cause:** Browser caching or incorrect file paths.

**Fix:** Refresh the page with `Ctrl + F5` and verify the asset request in the Network tab.

---

## 10. Best Practices

1. Keep HTML templates in the `templates` directory.
2. Keep CSS, JavaScript, and images in the `static` directory.
3. Use `url_for()` to generate URLs for static assets and routes.
4. Use template inheritance to maintain a consistent layout.
5. Keep business logic in Python rather than placing it in templates.
6. Avoid disabling Jinja autoescaping for untrusted content.
7. Never expose secrets or sensitive files in the public static directory.
8. Use `debug=True` only during local development.
9. Organize larger applications using Flask Blueprints when appropriate.

---

## 11. Interview Questions

**Q1. What is a template in Flask?**

A template is an HTML file that can include dynamic values and control logic using the Jinja template engine.

**Q2. What does `render_template()` do?**

It renders a template and returns the generated HTML response.

**Q3. What is the default templates directory?**

`templates/`

**Q4. What is the default static files directory?**

`static/`

**Q5. Why do we use `url_for('static', filename='...')`?**

It generates the URL for a static asset using Flask's static-file configuration.

**Q6. What is Jinja?**

Jinja is a template engine used by Flask to generate dynamic content.

**Q7. What is template inheritance?**

It allows child templates to reuse a common parent layout and override specified blocks.

**Q8. What is the difference between `{{ }}` and `{% %}`?**

`{{ }}` displays an expression's value, while `{% %}` is used for template statements such as loops, conditions, and blocks.

**Q9. Can Flask serve CSS and JavaScript files?**

Yes. Flask serves static assets from the configured static directory by default.

**Q10. What is `TemplateNotFound`?**

It is an error raised when Flask/Jinja cannot locate a requested template.

---

## 12. Official Documentation

- Flask Templates: https://flask.palletsprojects.com/en/stable/quickstart/#rendering-templates
- Flask Static Files: https://flask.palletsprojects.com/en/stable/quickstart/#static-files
- Jinja Template Documentation: https://jinja.palletsprojects.com/en/stable/templates/

