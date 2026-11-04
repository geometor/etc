"""GEOMETOR construction model for X_929 = ISOGONAL CONJUGATE OF X_928."""

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


def construct_x_00929(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_929 = ISOGONAL CONJUGATE OF X_928 on reference triangle ABC."""
    X_928 = point_from_barycentrics(model, A, B, C, -0.81187287, 0.33079099, 0.48108187, ID="X_928", classes=["center"])
    X_929 = isogonal_conjugate(model, A, B, C, X_928, ID="X_929", classes=["selected", "target"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center", "incident"])
    central_line(model, X_102, X_516, 102, 516, incident=True)
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center", "incident"])
    central_line(model, X_103, X_515, 103, 515, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_101, X_522, 101, 522, incident=True)
    return promote_point_to_top(model, X_929)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_929 on the given reference triangle."""
    model = create_model('X_929 = ISOGONAL CONJUGATE OF X_928')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00929(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00929.json"))
    write_center_svg(
        model_acute,
        here / "x-00929.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
