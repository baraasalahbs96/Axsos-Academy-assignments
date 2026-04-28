Flask Routing Assignment
Understanding Routing — Axsos Academy | Python Stack 2026
 
Overview
A Flask server that handles 4 URL routes, including dynamic routes with variables and a custom 404 error handler.
 
Requirements
• Python 3.x
• Flask library
 
Installation
Install Flask:
pip install flask
 
Run the Server
python3 server.py
Then open your browser at: http://localhost:5000
 
Routes
URL	Response
localhost:5000/	"Hello World!"
localhost:5000/Champion	"Champion!"
localhost:5000/say/<name>	"Hi <name>!"
localhost:5000/repeat/<n>/<word>	word repeated n times
 
Bonus Features
• Ninja Bonus: <int:times> ensures the repeat value is always an integer
• Sensei Bonus: Any unknown route returns "Sorry! No response. Try again."
 
Examples
localhost:5000/say/Flask     →  Hi Flask!
localhost:5000/repeat/3/hello  →  hello hello hello
 
