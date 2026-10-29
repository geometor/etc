"""GEOMETOR construction model for X(881) = ISOGONAL CONJUGATE OF X(880)."""

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


def construct_x_00881(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(881) = ISOGONAL CONJUGATE OF X(880) on reference triangle ABC."""
    X_880 = point_from_barycentrics(model, A, B, C, 4.3698192, 0.10246315, -3.4722823, ID="X(880)", classes=["center"])
    X_881 = isogonal_conjugate(model, A, B, C, X_880, ID="X(881)", classes=["selected", "target"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X(512)", classes=["center", "incident"])
    central_line(model, X_39, X_512, 39, 512, incident=True)
    X_351 = eval_trilinear_point(model, A, B, C, 'a*(b**(2)- c**(2))*(b**(2)+ c**(2)- 2*a**(2))', ID="X(351)", classes=["center", "incident"])
    X_694 = eval_trilinear_point(model, A, B, C, 'a/(a**(4) - b**(2)*c**(2))', ID="X(694)", classes=["center", "incident"])
    central_line(model, X_351, X_694, 351, 694, incident=True)
    return promote_point_to_top(model, X_881)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(881) on the given reference triangle."""
    model = create_model('X(881) = ISOGONAL CONJUGATE OF X(880)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00881(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00881.json"))
    write_center_svg(
        model_acute,
        here / "x-00881.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
