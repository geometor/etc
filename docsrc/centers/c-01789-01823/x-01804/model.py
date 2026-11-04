"""GEOMETOR construction model for X_1804 = INVERSE MIMOSA TRANSFORM OF X_223."""

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
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01804(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1804 = INVERSE MIMOSA TRANSFORM OF X_223 on reference triangle ABC."""
    X_1804 = eval_trilinear_point(model, A, B, C, '(1 + cos(2*A))/(1 + cos(A))', ID="X_1804", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_7, X_21, 7, 21, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_3, X_77, 3, 77, incident=True)
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center", "incident"])
    central_line(model, X_36, X_269, 36, 269, incident=True)
    return promote_point_to_top(model, X_1804)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1804 on the given reference triangle."""
    model = create_model('X_1804 = INVERSE MIMOSA TRANSFORM OF X_223')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01804(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01804.json"))
    write_center_svg(
        model_acute,
        here / "x-01804.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
