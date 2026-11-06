"""GEOMETOR construction model for X_3103 = OUTER VERTEX OF THE BROCARD SQUARE."""

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
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03103(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3103 = OUTER VERTEX OF THE BROCARD SQUARE on reference triangle ABC."""
    X_3102 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  -  pi  /4)', ID="X_3102", classes=["center"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center"])
    X_3103 = reflection_in_point(model, X_3102, X_39, ID="X_3103", classes=["selected", "target"], guide=False)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    central_line(model, X_76, X_485, 76, 485, incident=True)
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    X_487 = eval_trilinear_point(model, A, B, C, '((cos(A))*(1 - csc(A)*sin(B)*sin(C)))', ID="X_487", classes=["center", "incident"])
    central_line(model, X_194, X_487, 194, 487, incident=True)
    return promote_point_to_top(model, X_3103)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3103 on the given reference triangle."""
    model = create_model('X_3103 = OUTER VERTEX OF THE BROCARD SQUARE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03103(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03103.json"))
    write_center_svg(
        model_acute,
        here / "x-03103.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
