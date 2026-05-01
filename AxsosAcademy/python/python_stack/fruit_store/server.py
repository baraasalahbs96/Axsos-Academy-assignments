from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    name = request.form.get('first_name') + " " + request.form.get('last_name')
    student_id = request.form.get('student_id')
    strawberry = int(request.form.get('strawberry', 0))
    raspberry = int(request.form.get('raspberry', 0))
    apple = int(request.form.get('apple', 0))
    
    total_count = strawberry + raspberry + apple
    
    print(f"Charging {name} for {total_count} fruits.")
    
    time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    
    return render_template("checkout.html", 
                           name=name, student_id=student_id, 
                           strawberry=strawberry, raspberry=raspberry, apple=apple,
                           total_count=total_count, time=time)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__ == "__main__":
    app.run(debug=True)