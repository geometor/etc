"""GEOMETOR construction model for X_2065 = ORION TRANSFORM OF X_98."""

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


def construct_x_02065(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2065 = ORION TRANSFORM OF X_98 on reference triangle ABC."""
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center"])
    X_2065 = isogonal_conjugate(model, A, B, C, X_114, ID="X_2065", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    central_line(model, X_98, X_325, 98, 325, incident=True)
    X_460 = eval_trilinear_point(model, A, B, C, '(sec(A))*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_460", classes=["center", "incident"])
    X_685 = eval_trilinear_point(model, A, B, C, '(1/(sec(B)*(sin(C))**(3) - sec(C)*(sin(B))**(3)))', ID="X_685", classes=["center", "incident"])
    central_line(model, X_460, X_685, 460, 685, incident=True)
    X_248 = eval_trilinear_point(model, A, B, C, 'sin(2*A)*sec(A +  omega  )', ID="X_248", classes=["center", "incident"])
    X_1570 = eval_trilinear_point(model, A, B, C, 'a*(cot(A) + cot(omega)  - 4*tan(omega)  )', ID="X_1570", classes=["center", "incident"])
    central_line(model, X_248, X_1570, 248, 1570, incident=True)
    return promote_point_to_top(model, X_2065)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2065 on the given reference triangle."""
    model = create_model('X_2065 = ORION TRANSFORM OF X_98')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02065(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02065.json"))
    write_center_svg(
        model_acute,
        here / "x-02065.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
