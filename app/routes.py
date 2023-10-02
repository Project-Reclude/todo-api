from flask import Blueprint, request, jsonify

from app.models import Point
from app.db import db


blueprint = Blueprint("routes", __name__)


@blueprint.route("/todo/new_point", methods=["POST"])
def new_point():
    data = request.get_json()

    if not data:
        return jsonify({"message": "no data provided"}), 400

    point = Point()

    point.num = data.get("num")
    point.date = data.get("date")
    point.category = data.get("category")
    point.body = data.get("body")
    point.completed = data.get("completed")
    point.due = data.get("due")

    db.session.add(point)
    try:
        db.session.commit()
        return jsonify({"message": "Point added successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@blueprint.route("/todo/get_points", methods=["GET"])
def get_points():
    data = request.get_json()

    if not data:
        points = Point.query.all()

    else:
        points = Point.query.filter_by(date=data.get("date"))

    if points:
        return jsonify({"points": [dict(point) for point in points]}), 200

    else:
        return jsonify({"message": "No points found"}), 404
