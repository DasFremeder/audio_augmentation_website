#!/usr/bin/env python3

from flask import Flask


def create_app():
    app = Flask(__name__)
    from audio_augmentation_website.routes import main
    app.amount = 1
    app.methods = []
    app.register_blueprint(main)

    return app
