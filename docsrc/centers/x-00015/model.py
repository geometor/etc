"""GEOMETOR construction model for X(15) = 1st ISODYNAMIC POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00015(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(15) = 1st ISODYNAMIC POINT on reference triangle ABC."""
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center"])
    X_15 = isogonal_conjugate(model, A, B, C, X_13, ID="X(15)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_14 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /3)', ID="X(14)", classes=["center", "incident"])
    central_line(model, X_2, X_14, 2, 14, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X(17)", classes=["center", "incident"])
    central_line(model, X_4, X_17, 4, 17, incident=True)
    return promote_point_to_top(model, X_15)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(15) on the given reference triangle."""
    model = create_model('X(15) = 1st ISODYNAMIC POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00015(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00015.json"))
    write_center_svg(
        model_acute,
        here / "x-00015.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
