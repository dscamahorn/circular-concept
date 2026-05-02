from flask import Flask
import config


def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = config.SECRET_KEY

    from app.routes import register_routes
    register_routes(app)

    return app


app = create_app()