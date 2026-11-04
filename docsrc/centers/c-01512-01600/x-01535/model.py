"""GEOMETOR construction model for X_1535 = ORTHOJOIN OF X_41."""

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
    gergonne_point_of,
    intersect_lines,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01535(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1535 = ORTHOJOIN OF X_41 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center"])
    X_117 = point_from_barycentrics(model, A, B, C, 0.19223485, -0.017045455, 0.82481061, ID="X_117", classes=["center"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center"])
    central_line(model, X_4, X_7, 4, 7)
    central_line(model, X_117, X_515, 117, 515)
    X_1535 = intersect_lines(model, X_4, X_7, X_117, X_515, ID="X_1535", classes=["selected", "target"])
    X_151 = eval_barycentric_point(model, A, B, C, 'a**(12) + a**(11)*(b + c) + a**(10)*b*c + a**(9)*(3*b**(3) - b**(2)*c - b*c**(2) + 3*c**(3)) - a**(8)*(3*b**(4) + b**(3)*c + b*c**(3) + 3*c**(4)) - 2*a**(7)*(7*b**(5) + b**(4)*c - 4*b**(3)*c**(2) - 4*b**(2)*c**(3) + b*c**(4) + 7*c**(5)) - 2*a**(6)*b*c*(b**(4) - 2*b**(3)*c - 6*b**(2)*c**(2) - 2*b*c**(3) + c**(4)) + 2*a**(5)*(7*b**(7) + b**(6)*c - 5*b**(5)*c**(2) - 3*b**(4)*c**(3) - 3*b**(3)*c**(4) - 5*b**(2)*c**(5) + b*c**(6) + 7*c**(7)) + a**(4)*(3*b**(8) + 2*b**(7)*c - 4*b**(6)*c**(2) - 2*b**(5)*c**(3) + 2*b**(4)*c**(4) - 2*b**(3)*c**(5) - 4*b**(2)*c**(6) + 2*b*c**(7) + 3*c**(8)) - a**(3)*(3*b**(9) - b**(8)*c + 8*b**(6)*c**(3) - 10*b**(5)*c**(4) - 10*b**(4)*c**(5) + 8*b**(3)*c**(6) - b*c**(8) + 3*c**(9)) + a**(2)*b*c*(b**(8) - 4*b**(7)*c - 12*b**(6)*c**(2) + 4*b**(5)*c**(3) + 22*b**(4)*c**(4) + 4*b**(3)*c**(5) - 12*b**(2)*c**(6) - 4*b*c**(7) + c**(8)) - a*(b**(11) + b**(10)*c - 3*b**(9)*c**(2) - 3*b**(8)*c**(3) + 2*b**(7)*c**(4) + 2*b**(6)*c**(5) + 2*b**(5)*c**(6) + 2*b**(4)*c**(7) - 3*b**(3)*c**(8) - 3*b**(2)*c**(9) + b*c**(10) + c**(11)) - b**(12) - b**(11)*c + 4*b**(10)*c**(2) + 3*b**(9)*c**(3) - 7*b**(8)*c**(4) - 2*b**(7)*c**(5) + 8*b**(6)*c**(6) - 2*b**(5)*c**(7) - 7*b**(4)*c**(8) + 3*b**(3)*c**(9) + 4*b**(2)*c**(10) - b*c**(11) - c**(12)', ID="X_151", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_151, X_517, 151, 517, incident=True)
    return promote_point_to_top(model, X_1535)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1535 on the given reference triangle."""
    model = create_model('X_1535 = ORTHOJOIN OF X_41')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01535(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01535.json"))
    write_center_svg(
        model_acute,
        here / "x-01535.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
