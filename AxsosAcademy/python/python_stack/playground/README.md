# Playground - Flask Assignment

A Flask web application that renders colored boxes based on URL parameters.

## Project Structure

```
playground/
├── plauground.py
├── README.md
├── static/
│   └── css/
│       └── plauground.css
└── templates/
    └── plauground.html
```

## Requirements

- Python 3.x
- Flask

## Installation

```bash
pip3 install flask
```

## How to Run

```bash
python3 server.py
```

Then open your browser and visit: `http://localhost:5000/play`

## Routes

|Route              |Description                 |Example                      |
|-------------------|----------------------------|-----------------------------|
|`/play`            |Shows 3 blue boxes          |`localhost:5000/play`        |
|`/play/<x>`        |Shows x blue boxes          |`localhost:5000/play/7`      |
|`/play/<x>/<color>`|Shows x boxes in given color|`localhost:5000/play/5/green`|

## Examples

- `localhost:5000/play` → 3 blue boxes
- `localhost:5000/play/7` → 7 blue boxes
- `localhost:5000/play/35` → 35 blue boxes
- `localhost:5000/play/5/green` → 5 green boxes
- `localhost:5000/play/35/red` → 35 red boxes

## Features

- ✅ Level 1: Render 3 blue boxes at `/play`
- ✅ Level 2: Render x blue boxes at `/play/<x>`
- ✅ Level 3: Render x colored boxes at `/play/<x>/<color>`
- ✅ Ninja Bonus: Single template used for all routes

## Technologies

- Python
- Flask
- HTML/CSS (External Stylesheet)
- Jinja2 Templates