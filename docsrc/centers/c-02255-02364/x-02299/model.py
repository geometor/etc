"""GEOMETOR construction model for X_2299 = X_2-ISOCONJUGATE OF X_1214."""

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
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02299(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2299 = X_2-ISOCONJUGATE OF X_1214 on reference triangle ABC."""
    X_307 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c)*(cos(A))/(b + c - a)', ID="X_307", classes=["center"])
    X_2299 = isogonal_conjugate(model, A, B, C, X_307, ID="X_2299", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_9, X_33, 9, 33, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_19, X_31, 19, 31, incident=True)
    return promote_point_to_top(model, X_2299)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2299 on the given reference triangle."""
    model = create_model('X_2299 = X_2-ISOCONJUGATE OF X_1214')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02299(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02299.json"))
    write_center_svg(
        model_acute,
        here / "x-02299.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
