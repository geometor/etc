"""GEOMETOR construction model for X_2157 = X_2-ISOCONJUGATE OF X_23."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02157(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2157 = X_2-ISOCONJUGATE OF X_23 on reference triangle ABC."""
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center"])
    X_896 = eval_trilinear_point(model, A, B, C, '2*a**(2) - b**(2) - c**(2)', ID="X_896", classes=["center"])
    X_2157 = cevapoint(model, A, B, C, X_38, X_896, ID="X_2157", classes=["selected", "target"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_67", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_67, X_71, 67, 71, incident=True)
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    central_line(model, X_38, X_163, 38, 163, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_1109 = eval_trilinear_point(model, A, B, C, '(sin(B - C))**(2)', ID="X_1109", classes=["center", "incident"])
    central_line(model, X_19, X_1109, 19, 1109, incident=True)
    return promote_point_to_top(model, X_2157)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2157 on the given reference triangle."""
    model = create_model('X_2157 = X_2-ISOCONJUGATE OF X_23')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02157(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02157.json"))
    write_center_svg(
        model_acute,
        here / "x-02157.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
