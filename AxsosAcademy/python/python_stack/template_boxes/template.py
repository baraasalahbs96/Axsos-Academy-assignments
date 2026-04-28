from flask import Flask, render_template

app = Flask(__name__)

# Level 1: localhost:5000/play –> show 3 blue boxes

@app.route('/play')
def play():
    return render_template('templatejinja.html', num=3, color='blue')

# Level 2: localhost:5000/play/<x> –> show x blue boxes

# Example: localhost:5000/play/7  –> 7 blue boxes

# Example: localhost:5000/play/35 –> 35 blue boxes

@app.route('/play/<x>')
def play_x(x):
    return render_template('templatejinja.html', num=int(x), color='blue')

# Level 3: localhost:5000/play/<x>/<color> –> show x boxes in given color

# Example: localhost:5000/play/5/green  –> 5 green boxes

# Example: localhost:5000/play/35/red   –> 35 red boxes

@app.route('/play/<x>/<color>')
def play_x_color(x, color):
    return render_template('templatejinja.html', num=int(x), color=color)

if __name__ == "__main__":
    app.run(debug=True)