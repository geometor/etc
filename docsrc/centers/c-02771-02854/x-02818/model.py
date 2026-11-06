"""GEOMETOR construction model for X_2818 = ISOGONAL CONJUGATE OF X_2734."""

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
    isogonal_conjugate,
    nine_point_center_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02818(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2818 = ISOGONAL CONJUGATE OF X_2734 on reference triangle ABC."""
    X_2734 = point_from_barycentrics(model, A, B, C, 1.0250803, 0.41976584, -0.44484619, ID="X_2734", classes=["center"])
    X_2818 = isogonal_conjugate(model, A, B, C, X_2734, ID="X_2818", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center", "incident"])
    central_line(model, X_3, X_102, 3, 102, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X_117", classes=["center", "incident"])
    central_line(model, X_5, X_117, 5, 117, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_151 = eval_barycentric_point(model, A, B, C, 'a**(12) + a**(11)*(b + c) + a**(10)*b*c + a**(9)*(3*b**(3) - b**(2)*c - b*c**(2) + 3*c**(3)) - a**(8)*(3*b**(4) + b**(3)*c + b*c**(3) + 3*c**(4)) - 2*a**(7)*(7*b**(5) + b**(4)*c - 4*b**(3)*c**(2) - 4*b**(2)*c**(3) + b*c**(4) + 7*c**(5)) - 2*a**(6)*b*c*(b**(4) - 2*b**(3)*c - 6*b**(2)*c**(2) - 2*b*c**(3) + c**(4)) + 2*a**(5)*(7*b**(7) + b**(6)*c - 5*b**(5)*c**(2) - 3*b**(4)*c**(3) - 3*b**(3)*c**(4) - 5*b**(2)*c**(5) + b*c**(6) + 7*c**(7)) + a**(4)*(3*b**(8) + 2*b**(7)*c - 4*b**(6)*c**(2) - 2*b**(5)*c**(3) + 2*b**(4)*c**(4) - 2*b**(3)*c**(5) - 4*b**(2)*c**(6) + 2*b*c**(7) + 3*c**(8)) - a**(3)*(3*b**(9) - b**(8)*c + 8*b**(6)*c**(3) - 10*b**(5)*c**(4) - 10*b**(4)*c**(5) + 8*b**(3)*c**(6) - b*c**(8) + 3*c**(9)) + a**(2)*b*c*(b**(8) - 4*b**(7)*c - 12*b**(6)*c**(2) + 4*b**(5)*c**(3) + 22*b**(4)*c**(4) + 4*b**(3)*c**(5) - 12*b**(2)*c**(6) - 4*b*c**(7) + c**(8)) - a*(b**(11) + b**(10)*c - 3*b**(9)*c**(2) - 3*b**(8)*c**(3) + 2*b**(7)*c**(4) + 2*b**(6)*c**(5) + 2*b**(5)*c**(6) + 2*b**(4)*c**(7) - 3*b**(3)*c**(8) - 3*b**(2)*c**(9) + b*c**(10) + c**(11)) - b**(12) - b**(11)*c + 4*b**(10)*c**(2) + 3*b**(9)*c**(3) - 7*b**(8)*c**(4) - 2*b**(7)*c**(5) + 8*b**(6)*c**(6) - 2*b**(5)*c**(7) - 7*b**(4)*c**(8) + 3*b**(3)*c**(9) + 4*b**(2)*c**(10) - b*c**(11) - c**(12)', ID="X_151", classes=["center", "incident"])
    central_line(model, X_4, X_151, 4, 151, incident=True)
    return promote_point_to_top(model, X_2818)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2818 on the given reference triangle."""
    model = create_model('X_2818 = ISOGONAL CONJUGATE OF X_2734')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02818(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02818.json"))
    write_center_svg(
        model_acute,
        here / "x-02818.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
