"""GEOMETOR construction model for X(339) = ISOTOMIC CONJUGATE OF X(250)."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00339(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(339) = ISOTOMIC CONJUGATE OF X(250) on reference triangle ABC."""
    X_250 = eval_trilinear_point(model, A, B, C, '(sec(A))*(csc(B - C))**(2)', ID="X(250)", classes=["center"])
    X_339 = isotomic_conjugate(model, A, B, C, X_250, ID="X(339)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_3, X_76, 3, 76, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X(127)", classes=["center", "incident"])
    central_line(model, X_115, X_127, 115, 127, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_265 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*csc(3*A)', ID="X(265)", classes=["center", "incident"])
    central_line(model, X_69, X_265, 69, 265, incident=True)
    return promote_point_to_top(model, X_339)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(339) on the given reference triangle."""
    model = create_model('X(339) = ISOTOMIC CONJUGATE OF X(250)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00339(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00339.json"))
    write_center_svg(
        model_acute,
        here / "x-00339.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
