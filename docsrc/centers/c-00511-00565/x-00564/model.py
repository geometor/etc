"""GEOMETOR construction model for X_564 = INTERSECTION OF LINES X_1X_1048 AND X(47,91)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00564(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_564 = INTERSECTION OF LINES X_1X_1048 AND X(47,91) on reference triangle ABC."""
    X_564 = eval_trilinear_point(model, A, B, C, 'cos(2*B - 2*C)', ID="X_564", classes=["selected", "target"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center", "incident"])
    central_line(model, X_47, X_91, 47, 91, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1048 = eval_trilinear_point(model, A, B, C, 'a**(7)*(b**(2) + b*c + c**(2)) + a**(6)*(b + c)*(b**(2) + b*c + c**(2)) - a**(5)*(2*b**(4) + b**(3)*c + b*c**(3) + 2*c**(4)) - 2*a**(4)*(b + c)**(3)*(b**(2) - b*c + c**(2)) + a**(3)*(b**(6) - b**(5)*c - 2*b**(4)*c**(2) - b**(3)*c**(3) - 2*b**(2)*c**(4) - b*c**(5) + c**(6)) + a**(2)*(b**(7) + 2*b**(6)*c - 2*b**(4)*c**(3) - 2*b**(3)*c**(4) + 2*b*c**(6) + c**(7)) + a*b*c*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) - b**(2)*c**(2)*(b - c)**(2)*(b + c)**(3)', ID="X_1048", classes=["center", "incident"])
    central_line(model, X_1, X_1048, 1, 1048, incident=True)
    return promote_point_to_top(model, X_564)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_564 on the given reference triangle."""
    model = create_model('X_564 = INTERSECTION OF LINES X_1X_1048 AND X(47,91)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00564(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00564.json"))
    write_center_svg(
        model_acute,
        here / "x-00564.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
