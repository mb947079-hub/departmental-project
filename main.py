from website import create_app
from flask import render_template

app = create_app()

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def home():
    return "<h2>Server running successfully!</h2>"

if __name__ == "__main__":
    app.run(debug=True)