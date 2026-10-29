"""GEOMETOR construction model for X(591) = 1st VAN LAMOEN PERPENDICULAR BISECTORS POINT."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00591(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(591) = 1st VAN LAMOEN PERPENDICULAR BISECTORS POINT on reference triangle ABC."""
    X_591 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2) - 2*a**(2) + 4*area*(A*B*C))', ID="X(591)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_372 = eval_trilinear_point(model, A, B, C, 'cos(A + pi /4)', ID="X(372)", classes=["center", "incident"])
    X_754 = eval_trilinear_point(model, A, B, C, 'a**(-1)*(b**(4)+ c**(4)) - a**(3)*(b**(0)+ c**(0))', ID="X(754)", classes=["center", "incident"])
    central_line(model, X_372, X_754, 372, 754, incident=True)
    return promote_point_to_top(model, X_591)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(591) on the given reference triangle."""
    model = create_model('X(591) = 1st VAN LAMOEN PERPENDICULAR BISECTORS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00591(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00591.json"))
    write_center_svg(
        model_acute,
        here / "x-00591.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
