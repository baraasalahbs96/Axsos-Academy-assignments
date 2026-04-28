# Flask Checkerboard Project

## Description
This project renders a dynamic checkerboard using Flask, Jinja templates, and CSS.

The app demonstrates:
- Passing parameters from URL to Flask routes
- Passing data from routes to templates
- Using Jinja for loops
- Linking static CSS files

---

## Project Structure

checkerboard.py -> Flask app  
templates/checkerboard.html -> HTML template  
static/css/checkerboard.css -> Stylesheet  

---

## How to Run

1. Install Flask

pip install flask

2. Run the server

python checkerboard.py

3. Open browser:

Default board (8x8):
http://localhost:5000/

8 rows × X columns:
http://localhost:5000/4

X rows × Y columns:
http://localhost:5000/10/10

BONUS colors:
http://localhost:5000/10/10/blue/yellow

---

## Learning Goals

- URL parameters in Flask
- Jinja loops
- Static files in Flask
- Dynamic HTML rendering