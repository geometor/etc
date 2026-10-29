"""GEOMETOR construction model for X(126) = X(111)-OF-MEDIAL-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00126(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(126) = X(111)-OF-MEDIAL-TRIANGLE on reference triangle ABC."""
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X(111)", classes=["center"])
    X_126 = complement(model, A, B, C, X_111, ID="X(126)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_2, X_99, 2, 99, incident=True)
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X(125)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_125, X_141, 125, 141, incident=True)
    X_625 = eval_trilinear_point(model, A, B, C, '(2*(b**(4) + c**(4) - b**(2)*c**(2)) - a**(2)*(b**(2) + c**(2)))/a', ID="X(625)", classes=["center", "incident"])
    X_858 = eval_barycentric_point(model, A, B, C, 'a**(4)*b**(2) - b**(6) + a**(4)*c**(2) - 2*a**(2)*b**(2)*c**(2) + b**(4)*c**(2) + b**(2)*c**(4) - c**(6)', ID="X(858)", classes=["center", "incident"])
    central_line(model, X_625, X_858, 625, 858, incident=True)
    return promote_point_to_top(model, X_126)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(126) on the given reference triangle."""
    model = create_model('X(126) = X(111)-OF-MEDIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00126(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00126.json"))
    write_center_svg(
        model_acute,
        here / "x-00126.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
