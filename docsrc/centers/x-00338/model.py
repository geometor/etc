"""GEOMETOR construction model for X(338) = CEVAPOINT OF X(115) AND X(125)."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00338(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(338) = CEVAPOINT OF X(115) AND X(125) on reference triangle ABC."""
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X(249)", classes=["center"])
    X_338 = isotomic_conjugate(model, A, B, C, X_249, ID="X(338)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(67)", classes=["center", "incident"])
    central_line(model, X_4, X_67, 4, 67, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_94 = eval_trilinear_point(model, A, B, C, 'csc(3*A)', ID="X(94)", classes=["center", "incident"])
    central_line(model, X_2, X_94, 2, 94, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X(127)", classes=["center", "incident"])
    central_line(model, X_115, X_127, 115, 127, incident=True)
    return promote_point_to_top(model, X_338)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(338) on the given reference triangle."""
    model = create_model('X(338) = CEVAPOINT OF X(115) AND X(125)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00338(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00338.json"))
    write_center_svg(
        model_acute,
        here / "x-00338.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
