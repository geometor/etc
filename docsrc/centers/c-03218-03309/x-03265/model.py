"""GEOMETOR construction model for X_3265 = ISOTOMIC CONJUGATE OF X_107."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03265(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3265 = ISOTOMIC CONJUGATE OF X_107 on reference triangle ABC."""
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center"])
    X_2525 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) - c**(4))*(b**(2) + c**(2) - a**(2)))', ID="X_2525", classes=["center"])
    X_3265 = midpoint(model, X_647, X_2525, ID="X_3265", classes=["selected", "target"], guide=False)
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_325, X_523, 325, 523, incident=True)
    X_441 = point_from_barycentrics(model, A, B, C, 0.74590002, 0.58940921, -0.33530923, ID="X_441", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_441, X_525, 441, 525, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_1304 = eval_trilinear_point(model, A, B, C, '(sin(A))/((tan(B) - tan(C))*(tan(B) + tan(C) - 2*tan(A)))', ID="X_1304", classes=["center", "incident"])
    central_line(model, X_99, X_1304, 99, 1304, incident=True)
    return promote_point_to_top(model, X_3265)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3265 on the given reference triangle."""
    model = create_model('X_3265 = ISOTOMIC CONJUGATE OF X_107')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03265(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03265.json"))
    write_center_svg(
        model_acute,
        here / "x-03265.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
