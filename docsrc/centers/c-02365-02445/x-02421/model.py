"""GEOMETOR construction model for X_2421 = ISOGONAL CONJUGATE OF X_2395."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02421(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2421 = ISOGONAL CONJUGATE OF X_2395 on reference triangle ABC."""
    X_2395 = eval_barycentric_point(model, A, B, C, '(b**(2) - c**(2))/(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X_2395", classes=["center"])
    X_2421 = isogonal_conjugate(model, A, B, C, X_2395, ID="X_2421", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_351 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))*(b**(2) + c**(2) - 2*a**(2)))', ID="X_351", classes=["center", "incident"])
    central_line(model, X_110, X_351, 110, 351, incident=True)
    X_648 = eval_trilinear_point(model, A, B, C, '1/(a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2)))', ID="X_648", classes=["center", "incident"])
    X_670 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(2) - c**(2)))', ID="X_670", classes=["center", "incident"])
    central_line(model, X_648, X_670, 648, 670, incident=True)
    return promote_point_to_top(model, X_2421)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2421 on the given reference triangle."""
    model = create_model('X_2421 = ISOGONAL CONJUGATE OF X_2395')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02421(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02421.json"))
    write_center_svg(
        model_acute,
        here / "x-02421.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
