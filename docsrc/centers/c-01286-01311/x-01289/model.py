"""GEOMETOR construction model for X_1289 = COLLINGS TRANSFORM OF X_25."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01289(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1289 = COLLINGS TRANSFORM OF X_25 on reference triangle ABC."""
    X_1289 = eval_trilinear_point(model, A, B, C, 'tan(A)*csc(B - C)/(sin(2*A) - tan(omega)  )', ID="X_1289", classes=["selected", "target"])
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_24, X_98, 24, 98, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X_127", classes=["center", "incident"])
    central_line(model, X_4, X_127, 4, 127, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_74 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - 2*cos(B)*cos(C))', ID="X_74", classes=["center", "incident"])
    central_line(model, X_66, X_74, 66, 74, incident=True)
    return promote_point_to_top(model, X_1289)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1289 on the given reference triangle."""
    model = create_model('X_1289 = COLLINGS TRANSFORM OF X_25')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01289(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01289.json"))
    write_center_svg(
        model_acute,
        here / "x-01289.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
