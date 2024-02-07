from flask import jsonify, request
from . import libro_api_blueprint
from .. import db
from ..models import Libro

# aqui se definen las rutas


@libro_api_blueprint.route("/api/libros", methods=["GET"])
def libros():
    libros = []
    for row in Libro.query.all():  # pyright: ignore [reportUnknownVariableType]
        libros.append(  # pyright: ignore [reportUnknownMemberType]
            row.to_json()  # pyright: ignore [reportUnknownMemberType,reportUnknownArgumentType]
        )

    response = jsonify({"results": libros})
    return response


@libro_api_blueprint.route("/api/libro/add", methods=["POST"])
def add_book():
    title = request.form["title"]
    libro = Libro()
    libro.title = title

    db.session.add(libro)
    db.session.commit()

    response = jsonify({"message": "Libro added", "libro": libro.to_json()})
    return response