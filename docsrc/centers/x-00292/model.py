"""GEOMETOR construction model for X(292) = X(1)-HIRST INVERSE OF X(291)."""

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
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00292(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(292) = X(1)-HIRST INVERSE OF X(291) on reference triangle ABC."""
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X(239)", classes=["center"])
    X_292 = isogonal_conjugate(model, A, B, C, X_239, ID="X(292)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    central_line(model, X_1, X_39, 1, 39, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X(87)", classes=["center", "incident"])
    central_line(model, X_9, X_87, 9, 87, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    central_line(model, X_37, X_86, 37, 86, incident=True)
    return promote_point_to_top(model, X_292)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(292) on the given reference triangle."""
    model = create_model('X(292) = X(1)-HIRST INVERSE OF X(291)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00292(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00292.json"))
    write_center_svg(
        model_acute,
        here / "x-00292.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
