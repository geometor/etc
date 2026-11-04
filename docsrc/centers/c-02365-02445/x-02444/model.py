"""GEOMETOR construction model for X_2444 = ISOGONAL CONJUGATE OF X_2418."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02444(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2444 = ISOGONAL CONJUGATE OF X_2418 on reference triangle ABC."""
    X_2418 = eval_trilinear_point(model, A, B, C, '(b*c*(2*a**(2) - b**(2) - c**(2))/((5*a**(2) - b**(2) - c**(2))*(b**(2) - c**(2))))', ID="X_2418", classes=["center"])
    X_2444 = isogonal_conjugate(model, A, B, C, X_2418, ID="X_2444", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_6, X_512, 6, 512, incident=True)
    X_691 = eval_trilinear_point(model, A, B, C, 'a/((b**(2) - c**(2))*(2*a**(2) - b**(2) - c**(2)))', ID="X_691", classes=["center", "incident"])
    X_2421 = eval_trilinear_point(model, A, B, C, '(sin(A))*(sin(2*B) + sin(2*C) - 2*(cot(A))*((sin(B))**(2) + (sin(C))**(2)))/(cot(B) - cot(C))', ID="X_2421", classes=["center", "incident"])
    central_line(model, X_691, X_2421, 691, 2421, incident=True)
    X_1499 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))*(b**(2) + c**(2) - 5*a**(2))', ID="X_1499", classes=["center", "incident"])
    X_1992 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2) - 5*a**(2))', ID="X_1992", classes=["center", "incident"])
    central_line(model, X_1499, X_1992, 1499, 1992, incident=True)
    return promote_point_to_top(model, X_2444)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2444 on the given reference triangle."""
    model = create_model('X_2444 = ISOGONAL CONJUGATE OF X_2418')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02444(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02444.json"))
    write_center_svg(
        model_acute,
        here / "x-02444.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
