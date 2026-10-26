# Jinja2 — Complete Notes for Flask

## 1. What is Jinja2?

**Jinja2** is a template engine for Python that allows us to generate dynamic HTML pages by embedding variables, conditions, loops, and expressions inside HTML templates.

Flask uses Jinja as its default template engine.

### Why do we use Jinja2?

- To display dynamic data on HTML pages.
- To use variables inside HTML.
- To implement conditions and loops.
- To reuse common HTML layouts.
- To separate Python backend logic from HTML presentation.

### Example

**Python (app.py)**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Jagat"
    return render_template("index.html", username=name)

if __name__ == "__main__":
    app.run(debug=True)
```

**HTML (templates/index.html)**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Jinja2 Example</title>
</head>
<body>
    <h1>Hello, {{ username }}!</h1>
</body>
</html>
```

**Output:**

```text
Hello, Jagat!
```

Here, `render_template()` loads the HTML template and passes data to it. Jinja2 replaces `{{ username }}` with the actual value.

---

## 2. Project Folder Structure

```text
my_flask_app/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── about.html
│   └── profile.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── images/
        └── logo.png
```

**Important:**
- `templates/` contains HTML files rendered by Jinja2.
- `static/` contains CSS, JavaScript, images, and other static assets.
- Flask automatically looks for templates inside the `templates/` directory by default.

---

## 3. Important Jinja2 Syntax

Jinja2 primarily uses three types of syntax.

### A. Variables — `{{ }}`

Used to display values.

```html
<h1>{{ name }}</h1>
<p>Age: {{ age }}</p>
```

Python:

```python
return render_template(
    "index.html",
    name="Jagat",
    age=21
)
```

### B. Statements — `{% %}`

Used for control flow, loops, conditions, and template inheritance.

```html
{% if age >= 18 %}
    <p>Adult</p>
{% else %}
    <p>Minor</p>
{% endif %}
```

### C. Comments — `{# #}`

Comments are not rendered in the final HTML.

```html
{# This is a Jinja2 comment #}
```

---

## 4. If-Else Conditions

Jinja2 supports conditional statements.

```html
{% if marks >= 90 %}
    <p>Grade A</p>
{% elif marks >= 75 %}
    <p>Grade B</p>
{% elif marks >= 40 %}
    <p>Grade C</p>
{% else %}
    <p>Fail</p>
{% endif %}
```

Python:

```python
@app.route("/result")
def result():
    return render_template("result.html", marks=85)
```

**Output:** `Grade B`

Use cases:
- Login/logout buttons.
- Showing success or error messages.
- Displaying user-specific information.
- Showing different results based on conditions.

---

## 5. For Loops

Jinja2 can iterate over lists and other iterable data.

Python:

```python
@app.route("/students")
def students():
    names = ["Jagat", "Rahul", "Aman"]
    return render_template("students.html", names=names)
```

HTML:

```html
<h2>Student List</h2>

<ul>
    {% for name in names %}
        <li>{{ name }}</li>
    {% endfor %}
</ul>
```

Output:
- Jagat
- Rahul
- Aman

### Loop Variables

```html
{% for name in names %}
    <p>{{ loop.index }}. {{ name }}</p>
{% endfor %}
```

Useful loop variables:
- `loop.index` — current iteration number, starting from 1.
- `loop.index0` — current iteration number, starting from 0.
- `loop.first` — true on the first iteration.
- `loop.last` — true on the last iteration.
- `loop.length` — total number of items.

### Empty Lists

```html
{% for name in names %}
    <p>{{ name }}</p>
{% else %}
    <p>No students found.</p>
{% endfor %}
```

The `else` block runs when the loop has no items.

---

## 6. Passing Dictionaries to Templates

Python:

```python
@app.route("/profile")
def profile():
    user = {
        "name": "Jagat",
        "role": "Engineering Student",
        "skills": ["Python", "Flask", "Machine Learning"]
    }

    return render_template("profile.html", user=user)
```

HTML:

```html
<h1>{{ user.name }}</h1>
<p>Role: {{ user.role }}</p>

<h3>Skills</h3>
{% for skill in user.skills %}
    <p>{{ skill }}</p>
{% endfor %}
```

You can access dictionary values using dot notation or bracket notation:

```html
{{ user.name }}
{{ user["name"] }}
```

---

## 7. Template Inheritance

Template inheritance lets multiple pages reuse a common layout.

### Step 1: Create `templates/base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>

    <header>
        <h1>My Flask Website</h1>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>Copyright 2026</p>
    </footer>

</body>
</html>
```

### Step 2: Create `templates/home.html`

```html
{% extends "base.html" %}

{% block title %}
Home Page
{% endblock %}

{% block content %}
<h2>Welcome to my website!</h2>
<p>This content belongs to the home page.</p>
{% endblock %}
```

### Step 3: Render the page

```python
@app.route("/")
def home():
    return render_template("home.html")
```

**Benefits:**
- Avoids repeating HTML.
- Makes layouts easier to maintain.
- Keeps headers, footers, and navigation consistent.

`{% extends %}` should normally appear before other template content.

---

## 8. Including Reusable Templates

The `include` statement inserts another template into the current template.

Example folder structure:

```text
templates/
├── base.html
├── home.html
└── components/
    └── navbar.html
```

In `home.html`:

```html
{% include "components/navbar.html" %}
<h1>Home Page</h1>
```

**Difference:**
- `extends` — inherits a parent layout.
- `include` — inserts a reusable template fragment.

---

## 9. Filters

Filters transform values before displaying them. Use the pipe symbol `|`.

```html
{{ name | upper }}
{{ name | lower }}
{{ name | title }}
{{ message | trim }}
{{ items | length }}
```

Examples:

| Filter | Purpose |
|---|---|
| `upper` | Converts text to uppercase |
| `lower` | Converts text to lowercase |
| `title` | Capitalizes each word |
| `trim` | Removes surrounding whitespace |
| `length` | Returns the length of a sequence or mapping |
| `default` | Supplies a fallback for an undefined value |
| `join` | Joins sequence items into a string |
| `replace` | Replaces matching text |
| `safe` | Marks text as safe HTML; use cautiously |

Example:

```html
<p>{{ name | upper }}</p>
<p>{{ skills | join(", ") }}</p>
<p>{{ username | default("Guest") }}</p>
```

If `name = "jagat"`, the output is `JAGAT`.

**Security note:** Avoid using `safe` with untrusted user input because it can allow HTML injection or cross-site scripting (XSS).

---

## 10. URL Generation with `url_for()`

Flask's `url_for()` function generates URLs for routes and static assets.

### Route URL

Python:

```python
@app.route("/about")
def about():
    return render_template("about.html")
```

HTML:

```html
<a href="{{ url_for('about') }}">About Us</a>
```

The argument is the **endpoint name**, usually the Python view function's name.

### Static Files

```html
<link rel="stylesheet"
      href="{{ url_for('static', filename='css/style.css') }}">

<script src="{{ url_for('static', filename='js/script.js') }}"></script>

<img src="{{ url_for('static', filename='images/logo.png') }}"
     alt="Logo">
```

Using `url_for()` is preferable to hardcoding paths because Flask generates the appropriate URL.

---

## 11. Forms and Flash Messages

Flask flash messages can be displayed inside Jinja2 templates.

Python:

```python
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-secret"

@app.route("/submit")
def submit():
    flash("Form submitted successfully!", "success")
    return redirect(url_for("home"))

@app.route("/")
def home():
    return render_template("home.html")
```

HTML:

```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}
        <p class="{{ category }}">{{ message }}</p>
    {% endfor %}
{% endwith %}
```

In production, use a strong secret key from environment configuration. Do not hardcode real secrets in source code.

---

## 12. Autoescaping and Security

Jinja2 normally autoescapes HTML templates rendered through Flask's standard template setup.

For example, if a variable contains:

```text
<script>alert('hello')</script>
```

Jinja2 normally displays it as escaped text instead of executing it as HTML.

### Best Practices

- Keep autoescaping enabled for HTML.
- Do not mark untrusted content as `safe`.
- Never put secrets in templates.
- Validate and authorize sensitive actions in the backend.
- Use CSRF protection for state-changing forms.
- Do not assume that hiding a button in HTML secures the associated route.
- Avoid using `|safe` unless the HTML has been appropriately sanitized.

---

## 13. Common Errors

### Error 1: TemplateNotFound

Example:

```text
jinja2.exceptions.TemplateNotFound: index.html
```

**Cause:** Flask cannot locate the template.

**Fix:** Check that the file exists at:

```text
project/
├── app.py
└── templates/
    └── index.html
```

Also check spelling and capitalization.

### Error 2: Undefined Variable

```html
<h1>{{ username }}</h1>
```

But Python passes `name` instead of `username`.

**Fix:**

```python
return render_template("index.html", username="Jagat")
```

Variable names must match.

### Error 3: Missing `render_template`

Incorrect:

```python
return "index.html"
```

This returns the literal string `index.html`.

Correct:

```python
return render_template("index.html")
```

### Error 4: Missing End Tag

Incorrect:

```html
{% if logged_in %}
    <p>Welcome!</p>
```

Correct:

```html
{% if logged_in %}
    <p>Welcome!</p>
{% endif %}
```

Remember to close `if`, `for`, and `block` statements correctly.

---

## 14. Mini Project: Student Dashboard

### `app.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    student = {
        "name": "Jagat",
        "course": "Computer Science",
        "skills": ["Python", "Flask", "SQL"]
    }

    return render_template("dashboard.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/dashboard.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ student.name }}!</h1>
    <p>Course: {{ student.course }}</p>

    <h2>Skills</h2>
    <ul>
        {% for skill in student.skills %}
            <li>{{ skill }}</li>
        {% else %}
            <li>No skills added yet.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Run the project

```bash
pip install flask
python app.py
```

Open `http://127.0.0.1:5000/` in your browser.

---

## 15. Interview Questions

### Q1. What is Jinja2?
Jinja2 is a Python template engine used to generate dynamic content, commonly HTML pages, from templates and application data.

### Q2. Why does Flask use Jinja2?
It integrates Python backend data with HTML templates and supports variables, loops, conditions, filters, and inheritance.

### Q3. What is the difference between `{{ }}` and `{% %}`?
`{{ }}` prints an expression's value. `{% %}` executes template statements such as loops and conditions.

### Q4. What is `render_template()`?
It is a Flask function that loads a template from the templates directory, renders it with supplied context, and returns the resulting response.

### Q5. What is template inheritance?
It allows child templates to reuse and override named blocks in a parent template.

### Q6. What is the difference between `include` and `extends`?
`include` inserts another template. `extends` establishes a parent-child template relationship.

### Q7. What are Jinja2 filters?
Filters transform values during rendering, such as converting text to uppercase with `upper`.

### Q8. What is autoescaping?
Autoescaping converts characters with special HTML meaning into safe representations, helping prevent HTML injection and XSS in supported contexts.

### Q9. What is `url_for()`?
It generates URLs for Flask endpoints or static files.

### Q10. What is the difference between Flask and Jinja2?
Flask is a web framework that handles routes, requests, and responses. Jinja2 is the template engine Flask uses to render dynamic pages.

---

## 16. Practice Tasks

- [ ] Display your name and course using template variables.
- [ ] Create an `if-else` block to show pass or fail.
- [ ] Render a list of five skills using a loop.
- [ ] Display a dictionary containing student information.
- [ ] Create a `base.html` layout and extend it in two pages.
- [ ] Use `url_for()` to link pages and load CSS.
- [ ] Display a flash message after a form submission.
- [ ] Build a mini student dashboard using Flask and Jinja2.

## Official Documentation

- Flask Templates: https://flask.palletsprojects.com/en/stable/templating/
- Jinja Documentation: https://jinja.palletsprojects.com/en/stable/
- Flask Quickstart: https://flask.palletsprojects.com/en/stable/quickstart/

**Learning order:** Variables → Conditions → Loops → Dictionaries → Filters → `url_for()` → Template Inheritance → Forms → Security → Mini Project.
