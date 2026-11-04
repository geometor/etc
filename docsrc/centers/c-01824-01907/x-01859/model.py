"""GEOMETOR construction model for X_1859 = ZOSMA TRANSFORM OF X_226."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01859(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1859 = ZOSMA TRANSFORM OF X_226 on reference triangle ABC."""
    X_1859 = eval_trilinear_point(model, A, B, C, 'tan(A)*((b + c)*cos(A) + b*cos(B) + c*cos(C))', ID="X_1859", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_19, X_25, 19, 25, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_4, X_65, 4, 65, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X_132", classes=["center", "incident"])
    central_line(model, X_11, X_132, 11, 132, incident=True)
    return promote_point_to_top(model, X_1859)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1859 on the given reference triangle."""
    model = create_model('X_1859 = ZOSMA TRANSFORM OF X_226')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01859(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01859.json"))
    write_center_svg(
        model_acute,
        here / "x-01859.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
