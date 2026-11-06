"""GEOMETOR construction model for X_3064 = ISOGONAL CONJUGATE OF X_1813."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03064(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3064 = ISOGONAL CONJUGATE OF X_1813 on reference triangle ABC."""
    X_1813 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) - cos(C))', ID="X_1813", classes=["center"])
    X_3064 = isogonal_conjugate(model, A, B, C, X_1813, ID="X_3064", classes=["selected", "target"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_230, X_231, 230, 231, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center", "incident"])
    central_line(model, X_19, X_649, 19, 649, incident=True)
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    central_line(model, X_243, X_522, 243, 522, incident=True)
    return promote_point_to_top(model, X_3064)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3064 on the given reference triangle."""
    model = create_model('X_3064 = ISOGONAL CONJUGATE OF X_1813')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03064(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03064.json"))
    write_center_svg(
        model_acute,
        here / "x-03064.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
