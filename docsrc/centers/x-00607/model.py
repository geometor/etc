"""GEOMETOR construction model for X(607) = ISOGONAL CONJUGATE OF X(348)."""

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
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00607(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(607) = ISOGONAL CONJUGATE OF X(348) on reference triangle ABC."""
    X_348 = eval_trilinear_point(model, A, B, C, 'cot(A)*(sec(A/2))**(2)', ID="X(348)", classes=["center"])
    X_607 = isogonal_conjugate(model, A, B, C, X_348, ID="X(607)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X(29)", classes=["center", "incident"])
    central_line(model, X_8, X_29, 8, 29, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    central_line(model, X_25, X_41, 25, 41, incident=True)
    return promote_point_to_top(model, X_607)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(607) on the given reference triangle."""
    model = create_model('X(607) = ISOGONAL CONJUGATE OF X(348)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00607(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00607.json"))
    write_center_svg(
        model_acute,
        here / "x-00607.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
