from flask import Flask
from views.user_view import User
app = Flask(__name__)

app.register_blueprint(user)

@app.route('/')
def home():
    return "Welcome to the API!"

if __name__ == '__main__':
    app.run(debug=True)
