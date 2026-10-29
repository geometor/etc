"""GEOMETOR construction model for X(425) = X(4)-HIRST INVERSE OF X(21)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00425(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(425) = X(4)-HIRST INVERSE OF X(21) on reference triangle ABC."""
    X_425 = eval_barycentric_point(model, A, B, C, '(a + b)*(a + c)*(a**(2) + b**(2) - c**(2))*(a**(2) - b**(2) + c**(2))*(a**(6) - a**(5)*b - a**(4)*b**(2) + a**(3)*b**(3) - a**(5)*c + a**(4)*b*c + a**(3)*b**(2)*c - b**(5)*c - a**(4)*c**(2) + a**(3)*b*c**(2) + 2*a**(2)*b**(2)*c**(2) - 2*a*b**(3)*c**(2) + a**(3)*c**(3) - 2*a*b**(2)*c**(3) + 2*b**(3)*c**(3) - b*c**(5))', ID="X(425)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_243 = eval_barycentric_point(model, A, B, C, '(a - b - c)*(a**(4) - a**(2)*(b**(2) - b*c + c**(2)) - b*c*(b - c)**(2))/(a**(2) - b**(2) - c**(2))', ID="X(243)", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X(662)", classes=["center", "incident"])
    central_line(model, X_243, X_662, 243, 662, incident=True)
    return promote_point_to_top(model, X_425)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(425) on the given reference triangle."""
    model = create_model('X(425) = X(4)-HIRST INVERSE OF X(21)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00425(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00425.json"))
    write_center_svg(
        model_acute,
        here / "x-00425.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
