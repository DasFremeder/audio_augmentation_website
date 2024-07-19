#!/usr/bin/env python3

from flask import Blueprint, abort, render_template, request, current_app
from audio_augmentation_website.augmentation import search_for_method, bulk_process
main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index():
    return render_template(
        "index.html"
    )

@main.get("/function/<string:function_name>")
def parameter_api(function_name: str):
    print(function_name)
    _, plist = search_for_method(function_name)
    return plist

