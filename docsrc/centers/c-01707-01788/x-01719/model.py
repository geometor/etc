"""GEOMETOR construction model for X_1719 = MIMOSA TRANSFORM OF X_37."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01719(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1719 = MIMOSA TRANSFORM OF X_37 on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_191 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(b*c + c*a + a*b) + b**(3) + c**(3) - a**(3)', ID="X_191", classes=["center"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center"])
    X_407 = point_from_barycentrics(model, A, B, C, 0.10813862, 0.19355731, 0.69830407, ID="X_407", classes=["center"])
    central_line(model, X_10, X_191, 10, 191)
    central_line(model, X_46, X_407, 46, 407)
    X_1719 = intersect_lines(model, X_10, X_191, X_46, X_407, ID="X_1719", classes=["selected", "target"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    X_846 = eval_trilinear_point(model, A, B, C, '(- a**(2) + b**(2) + c**(2) + b*c + c*a + a*b)', ID="X_846", classes=["center", "incident"])
    central_line(model, X_165, X_846, 165, 846, incident=True)
    return promote_point_to_top(model, X_1719)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1719 on the given reference triangle."""
    model = create_model('X_1719 = MIMOSA TRANSFORM OF X_37')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01719(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01719.json"))
    write_center_svg(
        model_acute,
        here / "x-01719.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
