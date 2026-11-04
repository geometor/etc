"""GEOMETOR construction model for X_2000 = ORTHOCORRESPONDENT OF X_19."""

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
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02000(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2000 = ORTHOCORRESPONDENT OF X_19 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center"])
    central_line(model, X_1, X_2, 1, 2)
    central_line(model, X_33, X_63, 33, 63)
    X_2000 = intersect_lines(model, X_1, X_2, X_33, X_63, ID="X_2000", classes=["selected", "target"])
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center", "incident"])
    X_1004 = eval_trilinear_point(model, A, B, C, 'a**(5) - 2*a**(4)*(b + c) + 2*a**(2)*(b**(3) + c**(3)) - a*(b**(2) + c**(2))**(2) + 2*b*c*(b - c)*(b**(2) - c**(2))', ID="X_1004", classes=["center", "incident"])
    central_line(model, X_241, X_1004, 241, 1004, incident=True)
    return promote_point_to_top(model, X_2000)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2000 on the given reference triangle."""
    model = create_model('X_2000 = ORTHOCORRESPONDENT OF X_19')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02000(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02000.json"))
    write_center_svg(
        model_acute,
        here / "x-02000.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
