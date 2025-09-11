from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    title = "Megadeth"
    es_admin = True
    return render_template('index.html', title=title, albumsList=["Rust in Peace", "Countdown to Extinction", "Youthanasia", "Cryptic Writings"])

if __name__ == '__main__':
    app.run('localhost', 8080, debug=True)