from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super_secret_ninja_key'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        session['moves'] = 0
        session['game_over'] = False
        session['message'] = ""

    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if session.get('game_over'):
        return redirect('/')

    building = request.form['building']
    
    building_config = {
        'farm': (10, 20),
        'cave': (5, 10),
        'house': (2, 5),
        'casino': (-50, 50)
    }

    if building in building_config:
        min_gold, max_gold = building_config[building]
        earned = random.randint(min_gold, max_gold)
        session['gold'] += earned
        session['moves'] += 1
        
        time_now = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        if earned >= 0:
            activity = {
                'class': 'text-success',
                'text': f"Earned {earned} golds from the {building}! ({time_now})"
            }
        else:
            activity = {
                'class': 'text-danger',
                'text': f"Entered a casino and lost {abs(earned)} golds... Ouch. ({time_now})"
            }
        
        session['activities'].insert(0, activity)

        if session['gold'] >= 500:
            session['game_over'] = True
            session['message'] = "WINNER! You reached 500 gold!"
        elif session['moves'] >= 15:
            session['game_over'] = True
            session['message'] = "GAME OVER! You ran out of moves."

    session.modified = True
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)