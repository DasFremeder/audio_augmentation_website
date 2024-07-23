#!/usr/bin/env python3

from flask import Blueprint, abort, render_template, request, current_app
from audio_augmentation_website.augmentation import search_for_method, bulk_process
main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index():
    return render_template(
        "index.html"
    )

@main.post("/upload")
def file_return():
    print("Posted")
    if request.method == "POST":
        print(request.files)
        f = request.files['file']
        f.save(f"audio_augmentation_website/uploaded_files/{f.filename}")
        return render_template("checkbox.html")


@main.get("/function/<string:function_name>")
def parameter_api(function_name: str):
    print(function_name)
    _, plist = search_for_method(function_name)
    return plist

