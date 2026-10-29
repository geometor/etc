"""GEOMETOR construction model for X(303) = ISOTOMIC CONJUGATE OF 2nd NAPOLEON POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00303(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(303) = ISOTOMIC CONJUGATE OF 2nd NAPOLEON POINT on reference triangle ABC."""
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A - pi /6)', ID="X(18)", classes=["center"])
    X_303 = isotomic_conjugate(model, A, B, C, X_18, ID="X(303)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X(17)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_17, X_76, 17, 76, incident=True)
    X_13 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /3)', ID="X(13)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_13, X_99, 13, 99, incident=True)
    return promote_point_to_top(model, X_303)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(303) on the given reference triangle."""
    model = create_model('X(303) = ISOTOMIC CONJUGATE OF 2nd NAPOLEON POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00303(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00303.json"))
    write_center_svg(
        model_acute,
        here / "x-00303.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
