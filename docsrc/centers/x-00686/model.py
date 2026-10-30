"""GEOMETOR construction model for X(686) = CROSSDIFFERENCE OF X(4) AND X(110)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00686(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(686) = CROSSDIFFERENCE OF X(4) AND X(110) on reference triangle ABC."""
    X_686 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))*(a**(2) - b**(2) - c**(2))*(a**(4)*(b**(2) + c**(2)) - 2*a**(2)*(b**(4) - b**(2)*c**(2) + c**(4)) + (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X(686)", classes=["selected", "target"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center", "incident"])
    central_line(model, X_115, X_125, 115, 125, incident=True)
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X(184)", classes=["center", "incident"])
    X_351 = point_from_barycentrics(model, A, B, C, -1.104798, 0.16783217, 1.9369658, ID="X(351)", classes=["center", "incident"])
    central_line(model, X_184, X_351, 184, 351, incident=True)
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X(520)", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X(647)", classes=["center", "incident"])
    central_line(model, X_520, X_647, 520, 647, incident=True)
    return promote_point_to_top(model, X_686)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(686) on the given reference triangle."""
    model = create_model('X(686) = CROSSDIFFERENCE OF X(4) AND X(110)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00686(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00686.json"))
    write_center_svg(
        model_acute,
        here / "x-00686.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
