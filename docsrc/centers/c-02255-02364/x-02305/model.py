"""GEOMETOR construction model for X_2305 = X_2-ISOCONJUGATE OF X_1247."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02305(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2305 = X_2-ISOCONJUGATE OF X_1247 on reference triangle ABC."""
    X_1400 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))*(b + c)', ID="X_1400", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_2305 = ceva_conjugate(model, A, B, C, X_1400, X_6, ID="X_2305", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    central_line(model, X_37, X_171, 37, 171, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_199 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) + (b**(2) + c**(2) - a**(2))*(b*c + c*a + a*b)))', ID="X_199", classes=["center", "incident"])
    central_line(model, X_31, X_199, 31, 199, incident=True)
    return promote_point_to_top(model, X_2305)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2305 on the given reference triangle."""
    model = create_model('X_2305 = X_2-ISOCONJUGATE OF X_1247')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02305(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02305.json"))
    write_center_svg(
        model_acute,
        here / "x-02305.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
