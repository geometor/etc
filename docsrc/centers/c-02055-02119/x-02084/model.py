"""GEOMETOR construction model for X_2084 = PK-TRANSFORM OF X_31."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02084(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2084 = PK-TRANSFORM OF X_31 on reference triangle ABC."""
    X_661 = eval_trilinear_point(model, A, B, C, 'cot(B) - cot(C)', ID="X_661", classes=["center"])
    X_798 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) - c**(2))', ID="X_798", classes=["center"])
    X_2084 = crosspoint(model, A, B, C, X_661, X_798, ID="X_2084", classes=["selected", "target"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_514, X_661, 514, 661, incident=True)
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X_667", classes=["center", "incident"])
    X_788 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(3) - c**(3))', ID="X_788", classes=["center", "incident"])
    central_line(model, X_667, X_788, 667, 788, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_1500 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)', ID="X_1500", classes=["center", "incident"])
    central_line(model, X_512, X_1500, 512, 1500, incident=True)
    return promote_point_to_top(model, X_2084)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2084 on the given reference triangle."""
    model = create_model('X_2084 = PK-TRANSFORM OF X_31')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02084(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02084.json"))
    write_center_svg(
        model_acute,
        here / "x-02084.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
