"""GEOMETOR construction model for X_3432 = X_5-VERTEX CONJUGATE OF X_5."""

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
    isogonal_conjugate,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03432(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3432 = X_5-VERTEX CONJUGATE OF X_5 on reference triangle ABC."""
    X_2888 = eval_barycentric_point(model, A, B, C, 'a**(10) - 3*a**(8)*(b**(2) + c**(2)) + a**(6)*(4*b**(4) + 5*b**(2)*c**(2) + 4*c**(4)) - 2*a**(4)*(2*b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + 2*c**(6)) + 3*a**(2)*(b**(8) - b**(6)*c**(2) - b**(2)*c**(6) + c**(8)) - (b**(2) - c**(2))**(4)*(b**(2) + c**(2))', ID="X_2888", classes=["center"])
    X_3432 = isogonal_conjugate(model, A, B, C, X_2888, ID="X_3432", classes=["selected", "target"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    X_52 = eval_trilinear_point(model, A, B, C, 'cos(2*A)*cos(B - C)', ID="X_52", classes=["center", "incident"])
    central_line(model, X_49, X_52, 49, 52, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_1601 = point_from_barycentrics(model, A, B, C, 0.43272298, 0.23120612, 0.3360709, ID="X_1601", classes=["center", "incident"])
    central_line(model, X_5, X_1601, 5, 1601, incident=True)
    return promote_point_to_top(model, X_3432)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3432 on the given reference triangle."""
    model = create_model('X_3432 = X_5-VERTEX CONJUGATE OF X_5')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03432(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03432.json"))
    write_center_svg(
        model_acute,
        here / "x-03432.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
