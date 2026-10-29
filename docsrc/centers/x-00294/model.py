"""GEOMETOR construction model for X(294) = ISOGONAL CONJUGATE OF X(241)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00294(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(294) = ISOGONAL CONJUGATE OF X(241) on reference triangle ABC."""
    X_241 = eval_trilinear_point(model, A, B, C, '(b**(2) + c**(2) - a*b - a*c)/(a - b - c)', ID="X(241)", classes=["center"])
    X_294 = isogonal_conjugate(model, A, B, C, X_241, ID="X(294)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_6, X_7, 6, 7, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X(41)", classes=["center", "incident"])
    central_line(model, X_1, X_41, 1, 41, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '(cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X(218)", classes=["center", "incident"])
    central_line(model, X_4, X_218, 4, 218, incident=True)
    return promote_point_to_top(model, X_294)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(294) on the given reference triangle."""
    model = create_model('X(294) = ISOGONAL CONJUGATE OF X(241)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00294(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00294.json"))
    write_center_svg(
        model_acute,
        here / "x-00294.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
