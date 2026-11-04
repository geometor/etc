"""GEOMETOR construction model for X_1796 = INVERSE MIMOSA TRANSFORM OF X_37."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01796(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1796 = INVERSE MIMOSA TRANSFORM OF X_37 on reference triangle ABC."""
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center"])
    X_1268 = point_from_barycentrics(model, A, B, C, 0.34742328, 0.33294731, 0.31962942, ID="X_1268", classes=["center"])
    central_line(model, X_35, X_42, 35, 42)
    central_line(model, X_27, X_1268, 27, 1268)
    X_1796 = intersect_lines(model, X_35, X_42, X_27, X_1268, ID="X_1796", classes=["selected", "target"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_1255 = point_from_barycentrics(model, A, B, C, 0.29086678, 0.3344968, 0.37463642, ID="X_1255", classes=["center", "incident"])
    central_line(model, X_57, X_1255, 57, 1255, incident=True)
    return promote_point_to_top(model, X_1796)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1796 on the given reference triangle."""
    model = create_model('X_1796 = INVERSE MIMOSA TRANSFORM OF X_37')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01796(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01796.json"))
    write_center_svg(
        model_acute,
        here / "x-01796.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
