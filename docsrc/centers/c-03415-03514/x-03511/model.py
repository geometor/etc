"""GEOMETOR construction model for X_3511 = INTERSECTION OF LINES X_3X_76 AND X_6X_694."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03511(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3511 = INTERSECTION OF LINES X_3X_76 AND X_6X_694 on reference triangle ABC."""
    X_3511 = eval_trilinear_point(model, A, B, C, '(a*(a**(6)*b**(4) - a**(4)*b**(6) - a**(4)*c**(6) + a**(6)*c**(4) + b**(4)*c**(6) + b**(6)*c**(4) - a**(2)*b**(2)*c**(6) + a**(2)*b**(4)*c**(4) - a**(2)*b**(6)*c**(2) - a**(4)*b**(2)*c**(4) - a**(4)*b**(4)*c**(2) + a**(6)*b**(2)*c**(2)))', ID="X_3511", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_3, X_76, 3, 76, incident=True)
    X_147 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(8) + (b**(2) + c**(2))*a**(6) - (2*b**(4) + 3*b**(2)*c**(2) + 2*c**(4))*a**(4) + (b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + c**(6))*a**(2) - b**(8) + b**(6)*c**(2) + b**(2)*c**(6) - c**(8))', ID="X_147", classes=["center", "incident"])
    X_446 = point_from_barycentrics(model, A, B, C, 5.470003, 3.521611, -7.991614, ID="X_446", classes=["center", "incident"])
    central_line(model, X_147, X_446, 147, 446, incident=True)
    X_237 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A +  omega  )', ID="X_237", classes=["center", "incident"])
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X_385", classes=["center", "incident"])
    central_line(model, X_237, X_385, 237, 385, incident=True)
    return promote_point_to_top(model, X_3511)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3511 on the given reference triangle."""
    model = create_model('X_3511 = INTERSECTION OF LINES X_3X_76 AND X_6X_694')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03511(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03511.json"))
    write_center_svg(
        model_acute,
        here / "x-03511.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
