"""GEOMETOR construction model for X(985) = ISOGONAL CONJUGATE OF X(984)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00985(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(985) = ISOGONAL CONJUGATE OF X(984) on reference triangle ABC."""
    X_984 = eval_trilinear_point(model, A, B, C, 'b**(2) + b*c + c**(2)', ID="X(984)", classes=["center"])
    X_985 = isogonal_conjugate(model, A, B, C, X_984, ID="X(985)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    central_line(model, X_1, X_32, 1, 32, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    central_line(model, X_2, X_31, 2, 31, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X(291)", classes=["center", "incident"])
    central_line(model, X_6, X_291, 6, 291, incident=True)
    return promote_point_to_top(model, X_985)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(985) on the given reference triangle."""
    model = create_model('X(985) = ISOGONAL CONJUGATE OF X(984)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00985(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00985.json"))
    write_center_svg(
        model_acute,
        here / "x-00985.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
