"""GEOMETOR construction model for X_3118 = ISOGONAL CONJUGATE OF GtX(32)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_03118(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3118 = ISOGONAL CONJUGATE OF GtX(32) on reference triangle ABC."""
    X_3115 = eval_trilinear_point(model, A, B, C, '((b**(2) - c**(2))/(a**(3)*(b**(8) - c**(8))))', ID="X_3115", classes=["center"])
    X_3118 = isogonal_conjugate(model, A, B, C, X_3115, ID="X_3118", classes=["selected", "target"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_32, X_184, 32, 184, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    central_line(model, X_76, X_141, 76, 141, incident=True)
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X_694", classes=["center", "incident"])
    central_line(model, X_83, X_694, 83, 694, incident=True)
    return promote_point_to_top(model, X_3118)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3118 on the given reference triangle."""
    model = create_model('X_3118 = ISOGONAL CONJUGATE OF GtX(32)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03118(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03118.json"))
    write_center_svg(
        model_acute,
        here / "x-03118.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
