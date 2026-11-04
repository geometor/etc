"""GEOMETOR construction model for X_2200 = X_2-ISOCONJUGATE OF X_286."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02200(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2200 = X_2-ISOCONJUGATE OF X_286 on reference triangle ABC."""
    X_2200 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b + c)*(b**(2) + c**(2) - a**(2))', ID="X_2200", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_3, X_48, 3, 48, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_25, X_41, 25, 41, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_10, X_98, 10, 98, incident=True)
    return promote_point_to_top(model, X_2200)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2200 on the given reference triangle."""
    model = create_model('X_2200 = X_2-ISOCONJUGATE OF X_286')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02200(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02200.json"))
    write_center_svg(
        model_acute,
        here / "x-02200.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
