"""GEOMETOR construction model for X_3213 = X_57-CEVA CONJUGATE OF X_34."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03213(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3213 = X_57-CEVA CONJUGATE OF X_34 on reference triangle ABC."""
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_1394 = eval_trilinear_point(model, A, B, C, '(3*a**(4) - b**(4) - c**(4) - 2*a**(2)*b**(2) - 2*a**(2)*c**(2) + 2*b**(2)*c**(2))/(a - b - c)', ID="X_1394", classes=["center"])
    X_3213 = crosspoint(model, A, B, C, X_57, X_1394, ID="X_3213", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_19, X_56, 19, 56, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_208 = eval_trilinear_point(model, A, B, C, '((1 - sec(A))*(cos(B) + cos(C) - cos(A) - 1))', ID="X_208", classes=["center", "incident"])
    central_line(model, X_6, X_208, 6, 208, incident=True)
    X_154 = eval_trilinear_point(model, A, B, C, '(cos(A) - cos(B)*cos(C))*a**(2)', ID="X_154", classes=["center", "incident"])
    X_204 = eval_trilinear_point(model, A, B, C, '((tan(A))*(tan(B) + tan(C) - tan(A)))', ID="X_204", classes=["center", "incident"])
    central_line(model, X_154, X_204, 154, 204, incident=True)
    return promote_point_to_top(model, X_3213)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3213 on the given reference triangle."""
    model = create_model('X_3213 = X_57-CEVA CONJUGATE OF X_34')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03213(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03213.json"))
    write_center_svg(
        model_acute,
        here / "x-03213.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
