from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'Welcome to my web application!'

if _name_ == '_main_':
    app.run(debug=True)