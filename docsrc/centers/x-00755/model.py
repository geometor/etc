"""GEOMETOR construction model for X(755) = EVEN (0, 4) CIRCUMCIRCLE POINT."""

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


def construct_x_00755(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(755) = EVEN (0, 4) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_754 = point_from_barycentrics(model, A, B, C, -0.64313892, -0.11406714, 0.75720606, ID="X(754)", classes=["center"])
    X_755 = isogonal_conjugate(model, A, B, C, X_754, ID="X(755)", classes=["selected", "target"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_39, X_110, 39, 110, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_99, X_141, 99, 141, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    X_689 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(4) - c**(4)))', ID="X(689)", classes=["center", "incident"])
    central_line(model, X_76, X_689, 76, 689, incident=True)
    return promote_point_to_top(model, X_755)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(755) on the given reference triangle."""
    model = create_model('X(755) = EVEN (0, 4) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00755(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00755.json"))
    write_center_svg(
        model_acute,
        here / "x-00755.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
