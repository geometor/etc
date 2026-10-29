"""GEOMETOR construction model for X(393) = X(25)-CROSS CONJUGATE OF X(4)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00393(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(393) = X(25)-CROSS CONJUGATE OF X(4) on reference triangle ABC."""
    X_393 = eval_trilinear_point(model, A, B, C, 'sec(A) - csc(B)*csc(C)', ID="X(393)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    central_line(model, X_33, X_42, 33, 42, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_158 = point_from_barycentrics(model, A, B, C, 0.04776757, 0.099240104, 0.85299233, ID="X(158)", classes=["center", "incident"])
    central_line(model, X_37, X_158, 37, 158, incident=True)
    return promote_point_to_top(model, X_393)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(393) on the given reference triangle."""
    model = create_model('X(393) = X(25)-CROSS CONJUGATE OF X(4)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00393(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00393.json"))
    write_center_svg(
        model_acute,
        here / "x-00393.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
