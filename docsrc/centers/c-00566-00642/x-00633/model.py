"""GEOMETOR construction model for X_633 = ANTICOMPLEMENT OF X_61."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00633(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_633 = ANTICOMPLEMENT OF X_61 on reference triangle ABC."""
    X_61 = eval_trilinear_point(model, A, B, C, 'sin(A +  pi  /6)', ID="X_61", classes=["center"])
    X_633 = anticomplement(model, A, B, C, X_61, ID="X_633", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /6)', ID="X_18", classes=["center", "incident"])
    central_line(model, X_2, X_18, 2, 18, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_4, X_69, 4, 69, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_298 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*sin(A +  pi  /3)', ID="X_298", classes=["center", "incident"])
    central_line(model, X_3, X_298, 3, 298, incident=True)
    return promote_point_to_top(model, X_633)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_633 on the given reference triangle."""
    model = create_model('X_633 = ANTICOMPLEMENT OF X_61')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00633(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00633.json"))
    write_center_svg(
        model_acute,
        here / "x-00633.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
