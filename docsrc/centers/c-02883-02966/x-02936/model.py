"""GEOMETOR construction model for X_2936 = TANGENTIAL-ISOGONAL CONJUGATE OF X_187."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02936(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2936 = TANGENTIAL-ISOGONAL CONJUGATE OF X_187 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_67", classes=["center"])
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center"])
    central_line(model, X_3, X_67, 3, 67)
    central_line(model, X_22, X_99, 22, 99)
    X_2936 = intersect_lines(model, X_3, X_67, X_22, X_99, ID="X_2936", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_543 = eval_barycentric_point(model, A, B, C, '2*a**(4) - b**(4) - c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) + 4*b**(2)*c**(2)', ID="X_543", classes=["center", "incident"])
    central_line(model, X_25, X_543, 25, 543, incident=True)
    return promote_point_to_top(model, X_2936)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2936 on the given reference triangle."""
    model = create_model('X_2936 = TANGENTIAL-ISOGONAL CONJUGATE OF X_187')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02936(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02936.json"))
    write_center_svg(
        model_acute,
        here / "x-02936.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
