from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("dojo_survey.html")

@app.route('/result', methods=['POST'])
def process_survey():
    data = {
        "name": request.form.get('name'),
        "location": request.form.get('location'),
        "language": request.form.get('language'),
        "comments": request.form.get('comments'),
        "interests": request.form.getlist('interests') 
    }
    return render_template("result.html", survey_data=data)

if __name__ == "__main__":
    app.run(debug=True)