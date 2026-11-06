"""GEOMETOR construction model for X_2888 = ANTICOMPLEMENTARY CONJUGATE OF X_3."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02888(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2888 = ANTICOMPLEMENTARY CONJUGATE OF X_3 on reference triangle ABC."""
    X_2888 = eval_barycentric_point(model, A, B, C, 'a**(10) - 3*a**(8)*(b**(2) + c**(2)) + a**(6)*(4*b**(4) + 5*b**(2)*c**(2) + 4*c**(4)) - 2*a**(4)*(2*b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + 2*c**(6)) + 3*a**(2)*(b**(8) - b**(6)*c**(2) - b**(2)*c**(6) + c**(8)) - (b**(2) - c**(2))**(4)*(b**(2) + c**(2))', ID="X_2888", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_2, X_54, 2, 54, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X_93", classes=["center", "incident"])
    central_line(model, X_4, X_93, 4, 93, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_195 = eval_trilinear_point(model, A, B, C, 'a*(a**(8) + b**(8) + c**(8) - 4*a**(6)*(b**(2) + c**(2)) + a**(4)*(6*b**(4) + 6*c**(4) + 5*b**(2)*c**(2)) - a**(2)*(4*b**(6) + 4*c**(6) - b**(4)*c**(2) - b**(2)*c**(4)) - 2*b**(2)*c**(2)*(b**(4) + c**(4) - b**(2)*c**(2)))', ID="X_195", classes=["center", "incident"])
    central_line(model, X_5, X_195, 5, 195, incident=True)
    return promote_point_to_top(model, X_2888)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2888 on the given reference triangle."""
    model = create_model('X_2888 = ANTICOMPLEMENTARY CONJUGATE OF X_3')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02888(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02888.json"))
    write_center_svg(
        model_acute,
        here / "x-02888.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
