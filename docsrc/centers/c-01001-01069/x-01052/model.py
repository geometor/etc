"""GEOMETOR construction model for X_1052 = X_244-CEVA CONJUGATE OF X_1."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01052(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1052 = X_244-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1052 = ceva_conjugate(model, A, B, C, X_244, X_1, ID="X_1052", classes=["selected", "target"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_238, X_517, 238, 517, incident=True)
    X_765 = eval_trilinear_point(model, A, B, C, '(b - c) **(-2)', ID="X_765", classes=["center", "incident"])
    central_line(model, X_1, X_765, 1, 765, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_1054 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2) - a**(2) - 3*b*c + a*b + a*c', ID="X_1054", classes=["center", "incident"])
    central_line(model, X_513, X_1054, 513, 1054, incident=True)
    return promote_point_to_top(model, X_1052)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1052 on the given reference triangle."""
    model = create_model('X_1052 = X_244-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01052(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01052.json"))
    write_center_svg(
        model_acute,
        here / "x-01052.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
