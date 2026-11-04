"""GEOMETOR construction model for X_2892 = ANTICOMPLEMENTARY CONJUGATE OF X_23."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02892(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2892 = ANTICOMPLEMENTARY CONJUGATE OF X_23 on reference triangle ABC."""
    X_1177 = eval_trilinear_point(model, A, B, C, '(a/(b**(6) + c**(6) - a**(4)*b**(2) - a**(4)*c**(2) + 2*a**(2)*b**(2)*c**(2) - b**(4)*c**(2) - b**(2)*c**(4)))', ID="X_1177", classes=["center"])
    X_2892 = anticomplement(model, A, B, C, X_1177, ID="X_2892", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_67", classes=["center", "incident"])
    central_line(model, X_4, X_67, 4, 67, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_193 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cot(B) + cot(C) - cot(A))', ID="X_193", classes=["center", "incident"])
    central_line(model, X_66, X_193, 66, 193, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_1177, 2, 1177, incident=True)
    return promote_point_to_top(model, X_2892)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2892 on the given reference triangle."""
    model = create_model('X_2892 = ANTICOMPLEMENTARY CONJUGATE OF X_23')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02892(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02892.json"))
    write_center_svg(
        model_acute,
        here / "x-02892.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
