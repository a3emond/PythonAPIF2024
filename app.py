from flask import Flask
from views.user_view import user
app = Flask(__name__)

app.register_blueprint(user)

@app.route('/')
def home():
    return "flask runs on docker\n 1.0 - refactored"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
