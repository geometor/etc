"""GEOMETOR construction model for X_1718 = MIMOSA TRANSFORM OF X_36."""

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
    intersect_lines,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01718(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1718 = MIMOSA TRANSFORM OF X_36 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    central_line(model, X_1, X_5, 1, 5)
    central_line(model, X_34, X_46, 34, 46)
    X_1718 = intersect_lines(model, X_1, X_5, X_34, X_46, ID="X_1718", classes=["selected", "target"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_614 = eval_trilinear_point(model, A, B, C, 'a**(2) + b**(2) + c**(2) - 2*b*c', ID="X_614", classes=["center", "incident"])
    central_line(model, X_106, X_614, 106, 614, incident=True)
    return promote_point_to_top(model, X_1718)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1718 on the given reference triangle."""
    model = create_model('X_1718 = MIMOSA TRANSFORM OF X_36')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01718(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01718.json"))
    write_center_svg(
        model_acute,
        here / "x-01718.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
