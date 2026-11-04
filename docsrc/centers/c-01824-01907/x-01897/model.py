"""GEOMETOR construction model for X_1897 = ZOSMA TRANSFORM OF X_1054."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01897(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1897 = ZOSMA TRANSFORM OF X_1054 on reference triangle ABC."""
    X_1459 = eval_trilinear_point(model, A, B, C, '(b - c)*cos(A)', ID="X_1459", classes=["center"])
    X_1897 = isogonal_conjugate(model, A, B, C, X_1459, ID="X_1897", classes=["selected", "target"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    central_line(model, X_33, X_92, 33, 92, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_4, X_145, 4, 145, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    central_line(model, X_100, X_108, 100, 108, incident=True)
    return promote_point_to_top(model, X_1897)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1897 on the given reference triangle."""
    model = create_model('X_1897 = ZOSMA TRANSFORM OF X_1054')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01897(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01897.json"))
    write_center_svg(
        model_acute,
        here / "x-01897.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
