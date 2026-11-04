"""GEOMETOR construction model for X_821 = ISOGONAL CONJUGATE OF X_820."""

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


def construct_x_00821(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_821 = ISOGONAL CONJUGATE OF X_820 on reference triangle ABC."""
    X_820 = eval_trilinear_point(model, A, B, C, '((cos(A))**(2)*((cos(B))**(2) + (cos(C))**(2)))', ID="X_820", classes=["center"])
    X_821 = isogonal_conjugate(model, A, B, C, X_820, ID="X_821", classes=["selected", "target"])
    X_158 = eval_trilinear_point(model, A, B, C, '(sec(A))**(2)', ID="X_158", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    central_line(model, X_158, X_255, 158, 255, incident=True)
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    X_411 = eval_trilinear_point(model, A, B, C, '(cos(B)*cos(C) - (cos(A) + cos(B) + cos(C))*cos(A))', ID="X_411", classes=["center", "incident"])
    central_line(model, X_243, X_411, 243, 411, incident=True)
    X_774 = eval_trilinear_point(model, A, B, C, '(cos(B))**(2) + (cos(C))**(2)', ID="X_774", classes=["center", "incident"])
    X_823 = eval_trilinear_point(model, A, B, C, '1/((sec(B))**(2) - (sec(C))**(2))', ID="X_823", classes=["center", "incident"])
    central_line(model, X_774, X_823, 774, 823, incident=True)
    return promote_point_to_top(model, X_821)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_821 on the given reference triangle."""
    model = create_model('X_821 = ISOGONAL CONJUGATE OF X_820')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00821(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00821.json"))
    write_center_svg(
        model_acute,
        here / "x-00821.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
