"""GEOMETOR construction model for X(884) = ISOGONAL CONJUGATE OF X(883)."""

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


def construct_x_00884(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(884) = ISOGONAL CONJUGATE OF X(883) on reference triangle ABC."""
    X_883 = point_from_barycentrics(model, A, B, C, -1.5, 0.1, 2.4, ID="X(883)", classes=["center"])
    X_884 = isogonal_conjugate(model, A, B, C, X_883, ID="X(884)", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X(649)", classes=["center", "incident"])
    central_line(model, X_31, X_649, 31, 649, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    X_663 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(b + c - a)', ID="X(663)", classes=["center", "incident"])
    central_line(model, X_41, X_663, 41, 663, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X(55)", classes=["center", "incident"])
    X_650 = eval_trilinear_point(model, A, B, C, 'cos(B) - cos(C)', ID="X(650)", classes=["center", "incident"])
    central_line(model, X_55, X_650, 55, 650, incident=True)
    return promote_point_to_top(model, X_884)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(884) on the given reference triangle."""
    model = create_model('X(884) = ISOGONAL CONJUGATE OF X(883)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00884(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00884.json"))
    write_center_svg(
        model_acute,
        here / "x-00884.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
