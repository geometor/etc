"""GEOMETOR construction model for X_158 = X_19-CROSS CONJUGATE OF X_92."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00158(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_158 = X_19-CROSS CONJUGATE OF X_92 on reference triangle ABC."""
    X_158 = eval_trilinear_point(model, A, B, C, '(sec(A))**(2)', ID="X_158", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_1, X_29, 1, 29, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_4, X_65, 4, 65, incident=True)
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X_162", classes=["center", "incident"])
    central_line(model, X_47, X_162, 47, 162, incident=True)
    return promote_point_to_top(model, X_158)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_158 on the given reference triangle."""
    model = create_model('X_158 = X_19-CROSS CONJUGATE OF X_92')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00158(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00158.json"))
    write_center_svg(
        model_acute,
        here / "x-00158.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
