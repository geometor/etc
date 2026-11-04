"""GEOMETOR construction model for X_2429 = ISOGONAL CONJUGATE OF X_2403."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02429(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2429 = ISOGONAL CONJUGATE OF X_2403 on reference triangle ABC."""
    X_2403 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(3*a - b - c)/(2*a - b - c))', ID="X_2403", classes=["center"])
    X_2429 = isogonal_conjugate(model, A, B, C, X_2403, ID="X_2429", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1201 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) - 2*b*c + a*b + a*c))', ID="X_1201", classes=["center", "incident"])
    central_line(model, X_6, X_1201, 6, 1201, incident=True)
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    X_1293 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(3*a - b - c)))', ID="X_1293", classes=["center", "incident"])
    central_line(model, X_101, X_1293, 101, 1293, incident=True)
    return promote_point_to_top(model, X_2429)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2429 on the given reference triangle."""
    model = create_model('X_2429 = ISOGONAL CONJUGATE OF X_2403')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02429(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02429.json"))
    write_center_svg(
        model_acute,
        here / "x-02429.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
