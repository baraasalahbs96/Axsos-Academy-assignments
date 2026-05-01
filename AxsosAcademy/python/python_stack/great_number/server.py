from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'super_secret_key'

@app.route('/')
def index():
    if 'target_number' not in session:
        session['target_number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['message'] = None
        session['game_over'] = False
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if session['game_over']:
        return redirect('/')
    
    guess = int(request.form['guess'])
    session['attempts'] += 1
    
    if guess < session['target_number']:
        session['message'] = "Too low!"
        session['color'] = "bg-danger"
    elif guess > session['target_number']:
        session['message'] = "Too high!"
        session['color'] = "bg-danger"
    else:
        session['message'] = f"{session['target_number']} was the number!"
        session['color'] = "bg-success"
        session['game_over'] = True
        
    if session['attempts'] >= 5 and not session['game_over']:
        session['message'] = "You Lose! Game Over."
        session['color'] = "bg-danger"
        session['game_over'] = True
        
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)