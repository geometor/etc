"""GEOMETOR construction model for X_3450 = 1st SARAGOSSA POINT OF X_8."""

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
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03450(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3450 = 1st SARAGOSSA POINT OF X_8 on reference triangle ABC."""
    X_1329 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(2)/(a - b + c) + c**(2)/(a + b - c)))', ID="X_1329", classes=["center"])
    X_3450 = isogonal_conjugate(model, A, B, C, X_1329, ID="X_3450", classes=["selected", "target"])
    X_35 = eval_trilinear_point(model, A, B, C, '1 + 2*cos(A)', ID="X_35", classes=["center", "incident"])
    X_572 = eval_trilinear_point(model, A, B, C, '(cos(A - U))', ID="X_572", classes=["center", "incident"])
    central_line(model, X_35, X_572, 35, 572, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_1397 = eval_trilinear_point(model, A, B, C, '((sin(A)*sin(A/2))**(2))', ID="X_1397", classes=["center", "incident"])
    central_line(model, X_8, X_1397, 8, 1397, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1603 = point_from_barycentrics(model, A, B, C, 1.1738452, 1.1872659, -1.3611111, ID="X_1603", classes=["center", "incident"])
    central_line(model, X_6, X_1603, 6, 1603, incident=True)
    return promote_point_to_top(model, X_3450)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3450 on the given reference triangle."""
    model = create_model('X_3450 = 1st SARAGOSSA POINT OF X_8')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03450(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03450.json"))
    write_center_svg(
        model_acute,
        here / "x-03450.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
