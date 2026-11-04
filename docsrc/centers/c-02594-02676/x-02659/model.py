"""GEOMETOR construction model for X_2659 = CROSSDIFFERENCE OF PU(83)."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02659(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2659 = CROSSDIFFERENCE OF PU(83) on reference triangle ABC."""
    X_2659 = eval_trilinear_point(model, A, B, C, '(1/((sec(A) + sec(B))*(sec(A) + sec(C))) - 1/(sec(B) + sec(C))**(2))', ID="X_2659", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_1, X_29, 1, 29, incident=True)
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    X_410 = eval_barycentric_point(model, A, B, C, '(a + b) * (a + c) * (a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(8)*b**(2) - 3*a**(6)*b**(4) + 3*a**(4)*b**(6) - a**(2)*b**(8) + 3*a**(8)*b*c - a**(7)*b**(2)*c - 5*a**(6)*b**(3)*c + a**(5)*b**(4)*c + a**(4)*b**(5)*c + a**(3)*b**(6)*c + a**(2)*b**(7)*c - a*b**(8)*c + a**(8)*c**(2) - a**(7)*b*c**(2) - 3*a**(6)*b**(2)*c**(2) + a**(5)*b**(3)*c**(2) + 2*a**(4)*b**(4)*c**(2) + a**(3)*b**(5)*c**(2) + a**(2)*b**(6)*c**(2) - a*b**(7)*c**(2) - b**(8)*c**(2) - 5*a**(6)*b*c**(3) + a**(5)*b**(2)*c**(3) + 8*a**(4)*b**(3)*c**(3) - 2*a**(3)*b**(4)*c**(3) - a**(2)*b**(5)*c**(3) + a*b**(6)*c**(3) - 2*b**(7)*c**(3) - 3*a**(6)*c**(4) + a**(5)*b*c**(4) + 2*a**(4)*b**(2)*c**(4) - 2*a**(3)*b**(3)*c**(4) + a*b**(5)*c**(4) + b**(6)*c**(4) + a**(4)*b*c**(5) + a**(3)*b**(2)*c**(5) - a**(2)*b**(3)*c**(5) + a*b**(4)*c**(5) + 4*b**(5)*c**(5) + 3*a**(4)*c**(6) + a**(3)*b*c**(6) + a**(2)*b**(2)*c**(6) + a*b**(3)*c**(6) + b**(4)*c**(6) + a**(2)*b*c**(7) - a*b**(2)*c**(7) - 2*b**(3)*c**(7) - a**(2)*c**(8) - a*b*c**(8) - b**(2)*c**(8))', ID="X_410", classes=["center", "incident"])
    central_line(model, X_73, X_410, 73, 410, incident=True)
    X_185 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 - cos(A)*cos(B - C))', ID="X_185", classes=["center", "incident"])
    X_412 = eval_barycentric_point(model, A, B, C, '(a**(2) + b**(2) - c**(2)) * (a**(2) - b**(2) + c**(2)) * (a**(6) + a**(5)*b - 2*a**(4)*b**(2) - 2*a**(3)*b**(3) + a**(2)*b**(4) + a*b**(5) + a**(5)*c - a**(4)*b*c - a*b**(4)*c + b**(5)*c - 2*a**(4)*c**(2) + 2*a**(2)*b**(2)*c**(2) - 2*a**(3)*c**(3) - 2*b**(3)*c**(3) + a**(2)*c**(4) - a*b*c**(4) + a*c**(5) + b*c**(5))', ID="X_412", classes=["center", "incident"])
    central_line(model, X_185, X_412, 185, 412, incident=True)
    return promote_point_to_top(model, X_2659)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2659 on the given reference triangle."""
    model = create_model('X_2659 = CROSSDIFFERENCE OF PU(83)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02659(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02659.json"))
    write_center_svg(
        model_acute,
        here / "x-02659.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
