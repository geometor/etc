"""GEOMETOR construction model for X_2300 = X_2-ISOCONJUGATE OF X_1220."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02300(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2300 = X_2-ISOCONJUGATE OF X_1220 on reference triangle ABC."""
    X_2300 = eval_trilinear_point(model, A, B, C, 'a**(2)*(a*s + SA)', ID="X_2300", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_32, X_48, 32, 48, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_39, X_71, 39, 71, incident=True)
    return promote_point_to_top(model, X_2300)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2300 on the given reference triangle."""
    model = create_model('X_2300 = X_2-ISOCONJUGATE OF X_1220')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02300(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02300.json"))
    write_center_svg(
        model_acute,
        here / "x-02300.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
