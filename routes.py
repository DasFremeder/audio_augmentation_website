#!/usr/bin/env python3

from flask import Blueprint, abort, render_template, request, current_app, send_file
from audio_augmentation_website.augmentation import search_for_method, bulk_process
from audio_augmentation_website.unzipper import unzip,zip_output
main = Blueprint("main", __name__, url_prefix="/")

input_folder = "audio_augmentation_website/uploaded_files/user_name/"
output_folder = "audio_augmentation_website/output"
@main.get("/")
def get_index():
    return render_template(
        "index.html"
    )

@main.post("/checkbox")
def get_augmentation_methods():
    if request.method == "POST":
        f = request.files["file"] 
        save_path = f"{input_folder}{f.filename}"
        f.save(save_path) 
        unzip(save_path)
        return render_template("checkbox.html")

@main.post("/process")
def process():
    if request.method == "POST":
        f = request.form
        current_app.amount = int(f.get("amount"))
        for key in f.keys():
            if key != "amount":
                current_app.methods.append(key)
        bulk_process(input_folder,current_app.methods,output_folder,[],current_app.amount)   
        zip_output()    
        return render_template("loading.html")

@main.get("/download")
def download():
    if request.method == "GET":
        path = "output_archive.zip"
        return send_file(path)
# @main.get("/login")
# def get_index():
#     return render_template(
#         "login.html"
#     )
# @main.get("/loading")
# def get_index():
#     return render_template(
#         "loading.html"
#     )
# @main.get("/done")
# def get_index():
#     return render_template(
#         "finished.html"
#     )


@main.get("/function/<string:function_name>")
def parameter_api(function_name: str):
    print(function_name)
    _, plist = search_for_method(function_name)
    return plist

