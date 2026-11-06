"""GEOMETOR construction model for X_3304 = INTERSECTION OF LINES X_1X_3 AND X_495X_499."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03304(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3304 = INTERSECTION OF LINES X_1X_3 AND X_495X_499 on reference triangle ABC."""
    X_3304 = eval_trilinear_point(model, A, B, C, '3 - cos(A)', ID="X_3304", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_153 = eval_barycentric_point(model, A, B, C, 'a**(7) - a**(6)*(b + c) - a**(5)*(b**(2) - 7*b*c + c**(2)) + a**(4)*(b + c)*(b**(2) - 6*b*c + c**(2)) - a**(3)*(b**(4) + 2*b**(3)*c - 10*b**(2)*c**(2) + 2*b*c**(3) + c**(4)) + a**(2)*(b - c)**(2)*(b + c)*(b**(2) + 6*b*c + c**(2)) + a*(b**(2) - c**(2))**(2)*(b**(2) - 5*b*c + c**(2)) - (b - c)**(4)*(b + c)**(3)', ID="X_153", classes=["center", "incident"])
    central_line(model, X_11, X_153, 11, 153, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_386", classes=["center", "incident"])
    central_line(model, X_106, X_386, 106, 386, incident=True)
    return promote_point_to_top(model, X_3304)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3304 on the given reference triangle."""
    model = create_model('X_3304 = INTERSECTION OF LINES X_1X_3 AND X_495X_499')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03304(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03304.json"))
    write_center_svg(
        model_acute,
        here / "x-03304.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
