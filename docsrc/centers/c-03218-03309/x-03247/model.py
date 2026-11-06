"""GEOMETOR construction model for X_3247 = INTERSECTION OF LINES X_1X_6 AND X_2X_2321."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03247(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3247 = INTERSECTION OF LINES X_1X_6 AND X_2X_2321 on reference triangle ABC."""
    X_3247 = eval_trilinear_point(model, A, B, C, '(a + 3*b + 3*c)', ID="X_3247", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    X_347 = eval_trilinear_point(model, A, B, C, '((-1 - cos(A) + cos(B) + cos(C))*(sec(A/2))**(2))', ID="X_347", classes=["center", "incident"])
    central_line(model, X_226, X_347, 226, 347, incident=True)
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    X_966 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - 2*a*(b + c) - (b + c)**(2))', ID="X_966", classes=["center", "incident"])
    central_line(model, X_519, X_966, 519, 966, incident=True)
    return promote_point_to_top(model, X_3247)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3247 on the given reference triangle."""
    model = create_model('X_3247 = INTERSECTION OF LINES X_1X_6 AND X_2X_2321')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03247(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03247.json"))
    write_center_svg(
        model_acute,
        here / "x-03247.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
