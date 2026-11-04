"""GEOMETOR construction model for X_2215 = X_2-ISOCONJUGATE OF X_405."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02215(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2215 = X_2-ISOCONJUGATE OF X_405 on reference triangle ABC."""
    X_2215 = eval_barycentric_point(model, A, B, C, 'a**(2)/(a**(3) - a*(b + c)**(2) - 2*b*c*(b + c))', ID="X_2215", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_1, X_71, 1, 71, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_48, X_58, 48, 58, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_63, X_86, 63, 86, incident=True)
    return promote_point_to_top(model, X_2215)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2215 on the given reference triangle."""
    model = create_model('X_2215 = X_2-ISOCONJUGATE OF X_405')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02215(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02215.json"))
    write_center_svg(
        model_acute,
        here / "x-02215.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
