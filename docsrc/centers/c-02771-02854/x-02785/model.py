"""GEOMETOR construction model for X_2785 = ISOGONAL CONJUGATE OF X_2701."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02785(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2785 = ISOGONAL CONJUGATE OF X_2701 on reference triangle ABC."""
    X_2701 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(a**(3) + b**(3) + c**(3) - 2*a**(2)*b - 2*a**(2)*c + a*b*c)))', ID="X_2701", classes=["center"])
    X_2785 = isogonal_conjugate(model, A, B, C, X_2701, ID="X_2785", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    central_line(model, X_98, X_102, 98, 102, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    central_line(model, X_99, X_109, 99, 109, incident=True)
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X_117", classes=["center", "incident"])
    central_line(model, X_114, X_117, 114, 117, incident=True)
    return promote_point_to_top(model, X_2785)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2785 on the given reference triangle."""
    model = create_model('X_2785 = ISOGONAL CONJUGATE OF X_2701')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02785(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02785.json"))
    write_center_svg(
        model_acute,
        here / "x-02785.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
