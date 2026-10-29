"""GEOMETOR construction model for X(904) = X(238)-HIRST INVERSE OF X(256)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00904(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(904) = X(238)-HIRST INVERSE OF X(256) on reference triangle ABC."""
    X_904 = eval_trilinear_point(model, A, B, C, 'a**(2)/(a**(2) + b*c)', ID="X(904)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X(257)", classes=["center", "incident"])
    central_line(model, X_1, X_257, 1, 257, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X(238)", classes=["center", "incident"])
    central_line(model, X_21, X_238, 21, 238, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A + omega )', ID="X(237)", classes=["center", "incident"])
    central_line(model, X_31, X_237, 31, 237, incident=True)
    return promote_point_to_top(model, X_904)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(904) on the given reference triangle."""
    model = create_model('X(904) = X(238)-HIRST INVERSE OF X(256)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00904(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00904.json"))
    write_center_svg(
        model_acute,
        here / "x-00904.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
