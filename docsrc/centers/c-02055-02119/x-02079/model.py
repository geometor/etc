"""GEOMETOR construction model for X_2079 = INVERSE-IN-CIRCUMCIRCLE OF X_115."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02079(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2079 = INVERSE-IN-CIRCUMCIRCLE OF X_115 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center"])
    central_line(model, X_3, X_115, 3, 115)
    central_line(model, X_22, X_111, 22, 111)
    X_2079 = intersect_lines(model, X_3, X_115, X_22, X_111, ID="X_2079", classes=["selected", "target"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_24, X_112, 24, 112, incident=True)
    return promote_point_to_top(model, X_2079)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2079 on the given reference triangle."""
    model = create_model('X_2079 = INVERSE-IN-CIRCUMCIRCLE OF X_115')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02079(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02079.json"))
    write_center_svg(
        model_acute,
        here / "x-02079.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
