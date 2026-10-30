"""GEOMETOR construction model for X(699) = EVEN (- 4, - 2) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00699(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(699) = EVEN (- 4, - 2) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_698 = eval_barycentric_point(model, A, B, C, 'a**(2)*b**(4) + a**(2)*c**(4) - b**(4)*c**(2) - b**(2)*c**(4)', ID="X(698)", classes=["center"])
    X_699 = isogonal_conjugate(model, A, B, C, X_698, ID="X(699)", classes=["selected", "target"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_32, X_99, 32, 99, incident=True)
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A + omega )', ID="X(251)", classes=["center", "incident"])
    X_689 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(4) - c**(4)))', ID="X(689)", classes=["center", "incident"])
    central_line(model, X_251, X_689, 251, 689, incident=True)
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X(172)", classes=["center", "incident"])
    X_932 = point_from_barycentrics(model, A, B, C, 0.76211763, -0.28424928, 0.52213165, ID="X(932)", classes=["center", "incident"])
    central_line(model, X_172, X_932, 172, 932, incident=True)
    return promote_point_to_top(model, X_699)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(699) on the given reference triangle."""
    model = create_model('X(699) = EVEN (- 4, - 2) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00699(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00699.json"))
    write_center_svg(
        model_acute,
        here / "x-00699.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
