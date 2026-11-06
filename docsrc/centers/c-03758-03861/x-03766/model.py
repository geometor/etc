"""GEOMETOR construction model for X_3766 = X_3250com[T(bc, c²)]."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_03766(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3766 = X_3250com[T(bc, c²)] on reference triangle ABC."""
    X_660 = eval_trilinear_point(model, A, B, C, '1/((a**(2) - b*c)*(b - c))', ID="X_660", classes=["center"])
    X_3766 = isotomic_conjugate(model, A, B, C, X_660, ID="X_3766", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center", "incident"])
    central_line(model, X_2, X_665, 2, 665, incident=True)
    X_316 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2)))', ID="X_316", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_316, X_512, 316, 512, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_900 = eval_trilinear_point(model, A, B, C, '(b - c)*(b + c - 2*a)/a', ID="X_900", classes=["center", "incident"])
    central_line(model, X_75, X_900, 75, 900, incident=True)
    return promote_point_to_top(model, X_3766)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3766 on the given reference triangle."""
    model = create_model('X_3766 = X_3250com[T(bc, c²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03766(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03766.json"))
    write_center_svg(
        model_acute,
        here / "x-03766.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
