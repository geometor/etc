"""GEOMETOR construction model for X(695) = ISOGONAL CONJUGATE OF X(384)."""

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


def construct_x_00695(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(695) = ISOGONAL CONJUGATE OF X(384) on reference triangle ABC."""
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X(384)", classes=["center"])
    X_695 = isogonal_conjugate(model, A, B, C, X_384, ID="X(695)", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X(69)", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X(194)", classes=["center", "incident"])
    central_line(model, X_69, X_194, 69, 194, incident=True)
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A + omega )', ID="X(248)", classes=["center", "incident"])
    X_682 = point_from_barycentrics(model, A, B, C, 0.25664254, 0.47603357, 0.26732389, ID="X(682)", classes=["center", "incident"])
    central_line(model, X_248, X_682, 248, 682, incident=True)
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X(694)", classes=["center", "incident"])
    central_line(model, X_384, X_694, 384, 694, incident=True)
    return promote_point_to_top(model, X_695)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(695) on the given reference triangle."""
    model = create_model('X(695) = ISOGONAL CONJUGATE OF X(384)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00695(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00695.json"))
    write_center_svg(
        model_acute,
        here / "x-00695.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
