from flask import Flask

app = Flask(__name__)

#  localhost:5000/
@app.route('/')
def hello_world():
    return "Hello World!"

#  localhost:5000/Champion
@app.route('/Champion')
def champion():
    return "Champion!"

#  localhost:5000/say/<name>
@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name}!"
# Example: localhost:5000/say/Flask    –>  “Hi Flask!”
# Example: localhost:5000/say/Michael  –>  “Hi Michael!”
# Example: localhost:5000/say/john     –>  “Hi john!”

#  localhost:5000/repeat/<times>/<word>
@app.route('/repeat/<int:times>/<word>')
def repeat(times, word):
    return (word + " ") * times
# Example: localhost:5000/repeat/35/hello  –>  “hello “ repeated 35 times
# Example: localhost:5000/repeat/80/bye    –>  “bye “ repeated 80 times
# Example: localhost:5000/repeat/99/dogs   –>  “dogs “ repeated 99 times

# BONUS - route مجهول / any unknown route returns an error message
@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."
# Example: localhost:5000/anything  –>  “Sorry! No response. Try again.”

if __name__ == "__main__":
    app.run(debug=True)
