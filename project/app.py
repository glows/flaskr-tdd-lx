from flask import Flask

#
DATABSE = "flaskr.db"

#
app = Flask(__name__)

#
app.config.from_object(__name__)

@app.route("/")
def hello():
    return "Hello, world!"

if __name__ == "__main__":
    app.run()
