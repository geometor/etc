"""GEOMETOR construction model for X_1807 = INVERSE MIMOSA TRANSFORM OF X_484."""

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
    incenter_of,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01807(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1807 = INVERSE MIMOSA TRANSFORM OF X_484 on reference triangle ABC."""
    X_1807 = eval_trilinear_point(model, A, B, C, '1/(2 - sec(A))', ID="X_1807", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_101 = eval_trilinear_point(model, A, B, C, 'a/(b - c)', ID="X_101", classes=["center", "incident"])
    central_line(model, X_37, X_101, 37, 101, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_201 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(B - C))', ID="X_201", classes=["center", "incident"])
    central_line(model, X_3, X_201, 3, 201, incident=True)
    return promote_point_to_top(model, X_1807)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1807 on the given reference triangle."""
    model = create_model('X_1807 = INVERSE MIMOSA TRANSFORM OF X_484')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01807(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01807.json"))
    write_center_svg(
        model_acute,
        here / "x-01807.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
