"""GEOMETOR construction model for X_1021 = ISOGONAL CONJUGATE OF X_1020."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01021(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1021 = ISOGONAL CONJUGATE OF X_1020 on reference triangle ABC."""
    X_1020 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C))/(cos(B) - cos(C))', ID="X_1020", classes=["center"])
    X_1021 = isogonal_conjugate(model, A, B, C, X_1020, ID="X_1021", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center", "incident"])
    central_line(model, X_1, X_647, 1, 647, incident=True)
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_239, X_514, 239, 514, incident=True)
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_243, X_522, 243, 522, incident=True)
    return promote_point_to_top(model, X_1021)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1021 on the given reference triangle."""
    model = create_model('X_1021 = ISOGONAL CONJUGATE OF X_1020')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01021(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01021.json"))
    write_center_svg(
        model_acute,
        here / "x-01021.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
