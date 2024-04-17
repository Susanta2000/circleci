from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Flask Python"

@app.route("/user", methods=['GET'])
def get_user():
    user = {
        "Name": "Python",
        "Age": 2023
    }
    return user

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6000)