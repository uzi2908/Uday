from create_view import creating_view
from flask import Flask


def Create_app():

    app = Flask(__name__)

    creating_view(app)

    return app

if __name__ == '__main__':
    app = Create_app()
    app.run(debug=True)