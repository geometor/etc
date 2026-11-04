"""GEOMETOR construction model for X_1258 = ISOGONAL CONJUGATE OF X_1107."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01258(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1258 = ISOGONAL CONJUGATE OF X_1107 on reference triangle ABC."""
    X_1107 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2)) + b*c*(b + c))', ID="X_1107", classes=["center"])
    X_1258 = isogonal_conjugate(model, A, B, C, X_1107, ID="X_1258", classes=["selected", "target"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X_172", classes=["center", "incident"])
    central_line(model, X_81, X_172, 81, 172, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_330 = eval_trilinear_point(model, A, B, C, 'b*c/(a*b + a*c - b*c)', ID="X_330", classes=["center", "incident"])
    central_line(model, X_6, X_330, 6, 330, incident=True)
    X_213 = eval_trilinear_point(model, A, B, C, '(b + c)*a**(2)', ID="X_213", classes=["center", "incident"])
    X_274 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c)', ID="X_274", classes=["center", "incident"])
    central_line(model, X_213, X_274, 213, 274, incident=True)
    return promote_point_to_top(model, X_1258)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1258 on the given reference triangle."""
    model = create_model('X_1258 = ISOGONAL CONJUGATE OF X_1107')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01258(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01258.json"))
    write_center_svg(
        model_acute,
        here / "x-01258.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
