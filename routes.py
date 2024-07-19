#!/usr/bin/env python3

from flask import Blueprint, abort, render_template, request, current_app
from audio_augmentation_website.augmentation import search_for_method, bulk_process
main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def get_index():
    return render_template(
        "query_form.html",
        types=current_app.types,
        generations=current_app.generations,
    )

@main.get("/function/<str:function_name>")
def parameter_api(function_name: str):
    return search_for_method(function_name)


@main.route("/<int:pokemon_id>")
def pok_by_id(pokemon_id: int):
    try:
        data = [m for m in current_app.data if int(m["ID"]) == pokemon_id][0]
    except IndexError:
        abort(404)
    return render_template("details.html", data=data)
