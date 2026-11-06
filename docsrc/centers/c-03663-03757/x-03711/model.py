"""GEOMETOR construction model for X_3711 = X_3306com(EXTOUCH TRIANGLE)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    feuerbach_point_of,
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03711(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3711 = X_3306com(EXTOUCH TRIANGLE) on reference triangle ABC."""
    X_3711 = eval_barycentric_point(model, A, B, C, '(a*(b + c - a)*(2*b + 2*c - a))', ID="X_3711", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_8, X_11, 8, 11, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_9, X_55, 9, 55, incident=True)
    X_214 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)*(b**(2) + c**(2) - a**(2) - b*c)', ID="X_214", classes=["center", "incident"])
    X_956 = eval_trilinear_point(model, A, B, C, '(a**(3) - a*(b - c)**(2) - 2*b*c*(b + c))', ID="X_956", classes=["center", "incident"])
    central_line(model, X_214, X_956, 214, 956, incident=True)
    return promote_point_to_top(model, X_3711)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3711 on the given reference triangle."""
    model = create_model('X_3711 = X_3306com(EXTOUCH TRIANGLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03711(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03711.json"))
    write_center_svg(
        model_acute,
        here / "x-03711.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
