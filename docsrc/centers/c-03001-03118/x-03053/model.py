"""GEOMETOR construction model for X_3053 = INTERSECTION X_3X_6∩X_4X_230."""

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
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03053(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3053 = INTERSECTION X_3X_6∩X_4X_230 on reference triangle ABC."""
    X_2996 = eval_trilinear_point(model, A, B, C, '(b*c/(3*a**(2) - b**(2) - c**(2)))', ID="X_2996", classes=["center"])
    X_3053 = isogonal_conjugate(model, A, B, C, X_2996, ID="X_3053", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_24, X_112, 24, 112, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    central_line(model, X_4, X_230, 4, 230, incident=True)
    return promote_point_to_top(model, X_3053)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3053 on the given reference triangle."""
    model = create_model('X_3053 = INTERSECTION X_3X_6∩X_4X_230')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03053(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03053.json"))
    write_center_svg(
        model_acute,
        here / "x-03053.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
