"""GEOMETOR construction model for X_2205 = X_2-ISOCONJUGATE OF X_310."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02205(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2205 = X_2-ISOCONJUGATE OF X_310 on reference triangle ABC."""
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_1918 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b + c))', ID="X_1918", classes=["center"])
    X_2205 = ceva_conjugate(model, A, B, C, X_32, X_1918, ID="X_2205", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_31, X_32, 31, 32, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    central_line(model, X_37, X_82, 37, 82, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X_172", classes=["center", "incident"])
    central_line(model, X_81, X_172, 81, 172, incident=True)
    return promote_point_to_top(model, X_2205)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2205 on the given reference triangle."""
    model = create_model('X_2205 = X_2-ISOCONJUGATE OF X_310')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02205(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02205.json"))
    write_center_svg(
        model_acute,
        here / "x-02205.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
