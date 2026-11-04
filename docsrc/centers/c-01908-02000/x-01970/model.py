"""GEOMETOR construction model for X_1970 = CROSSSUM OF PU(38)."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01970(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1970 = CROSSSUM OF PU(38) on reference triangle ABC."""
    X_1970 = eval_trilinear_point(model, A, B, C, '(a*((sin(2*A))**(2) + sin(2*B)*sin(2*C)))', ID="X_1970", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_54, X_112, 54, 112, incident=True)
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    X_1625 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2)) / (b**(2) - c**(2))', ID="X_1625", classes=["center", "incident"])
    central_line(model, X_49, X_1625, 49, 1625, incident=True)
    return promote_point_to_top(model, X_1970)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1970 on the given reference triangle."""
    model = create_model('X_1970 = CROSSSUM OF PU(38)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01970(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01970.json"))
    write_center_svg(
        model_acute,
        here / "x-01970.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
