"""GEOMETOR construction model for X_3761 = X_2276com[T(bc, c²)]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03761(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3761 = X_2276com[T(bc, c²)] on reference triangle ABC."""
    X_751 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + 2*b*c)', ID="X_751", classes=["center"])
    X_3761 = isotomic_conjugate(model, A, B, C, X_751, ID="X_3761", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_1, X_76, 1, 76, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A-  omega  )', ID="X_183", classes=["center", "incident"])
    central_line(model, X_36, X_183, 36, 183, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_310 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b + c)', ID="X_310", classes=["center", "incident"])
    central_line(model, X_43, X_310, 43, 310, incident=True)
    return promote_point_to_top(model, X_3761)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3761 on the given reference triangle."""
    model = create_model('X_3761 = X_2276com[T(bc, c²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03761(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03761.json"))
    write_center_svg(
        model_acute,
        here / "x-03761.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
