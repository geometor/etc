"""GEOMETOR construction model for X(39) = BROCARD MIDPOINT."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00039(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(39) = BROCARD MIDPOINT on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    central_line(model, X_3, X_6, 3, 6)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center"])
    central_line(model, X_2, X_76, 2, 76)
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X(83)", classes=["center"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center"])
    central_line(model, X_83, X_99, 83, 99)
    X_39 = isogonal_conjugate(model, A, B, C, X_83, ID="X(39)", classes=["selected", "target"])
    return promote_point_to_top(model, X_39)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(39) on the given reference triangle."""
    model = create_model('X(39) = BROCARD MIDPOINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00039(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00039.json"))
    write_center_svg(
        model_acute,
        here / "x-00039.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
