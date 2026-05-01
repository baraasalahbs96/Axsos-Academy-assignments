from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'keep_it_secret_keep_it_safe' 

@app.route('/')
def index():
    if 'visits' not in session:
        session['visits'] = 0
    if 'counter' not in session:
        session['counter'] = 0
    
    session['visits'] += 1
    return render_template('index.html')

@app.route('/add_two', methods=['POST'])
def add_two():
    session['counter'] += 2
    return redirect('/')

@app.route('/increment_custom', methods=['POST'])
def increment_custom():
    increment_by = int(request.form.get('increment', 1))
    session['counter'] += increment_by
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)