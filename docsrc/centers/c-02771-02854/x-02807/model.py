"""GEOMETOR construction model for X_2807 = ISOGONAL CONJUGATE OF X_2723."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02807(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2807 = ISOGONAL CONJUGATE OF X_2723 on reference triangle ABC."""
    X_2723 = point_from_barycentrics(model, A, B, C, 1.0392316, 0.18668831, -0.22591991, ID="X_2723", classes=["center"])
    X_2807 = isogonal_conjugate(model, A, B, C, X_2723, ID="X_2807", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    central_line(model, X_55, X_103, 55, 103, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    central_line(model, X_1, X_185, 1, 185, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    central_line(model, X_101, X_102, 101, 102, incident=True)
    return promote_point_to_top(model, X_2807)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2807 on the given reference triangle."""
    model = create_model('X_2807 = ISOGONAL CONJUGATE OF X_2723')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02807(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02807.json"))
    write_center_svg(
        model_acute,
        here / "x-02807.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
