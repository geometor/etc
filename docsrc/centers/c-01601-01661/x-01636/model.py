"""GEOMETOR construction model for X_1636 = TRIPOLAR CENTROID OF X_3."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01636(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1636 = TRIPOLAR CENTROID OF X_3 on reference triangle ABC."""
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X_648", classes=["center"])
    X_1294 = eval_barycentric_point(model, A, B, C, '1/(a**(6)*(b**(2) + c**(2)) - a**(4)*(3*b**(4) - 4*b**(2)*c**(2) + 3*c**(4)) + 3*a**(2)*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2)*(b**(4) + 4*b**(2)*c**(2) + c**(4)))', ID="X_1294", classes=["center"])
    X_1636 = crosspoint(model, A, B, C, X_648, X_1294, ID="X_1636", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_110, X_112, 110, 112, incident=True)
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X_520", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center", "incident"])
    central_line(model, X_520, X_647, 520, 647, incident=True)
    X_1637 = eval_barycentric_point(model, A, B, C, 'tan(A)*(tan(B) - tan(C))*(tan(B) + tan(C) - 2*tan(A))', ID="X_1637", classes=["center", "incident"])
    X_1651 = point_from_barycentrics(model, A, B, C, 0.1117678, 0.1958099, 0.69242231, ID="X_1651", classes=["center", "incident"])
    central_line(model, X_1637, X_1651, 1637, 1651, incident=True)
    return promote_point_to_top(model, X_1636)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1636 on the given reference triangle."""
    model = create_model('X_1636 = TRIPOLAR CENTROID OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01636(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01636.json"))
    write_center_svg(
        model_acute,
        here / "x-01636.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
