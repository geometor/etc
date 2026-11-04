"""GEOMETOR construction model for X_1857 = ZOSMA TRANSFORM OF X_223."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01857(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1857 = ZOSMA TRANSFORM OF X_223 on reference triangle ABC."""
    X_1804 = eval_trilinear_point(model, A, B, C, '(1 + cos(2*A))/(1 + cos(A))', ID="X_1804", classes=["center"])
    X_1857 = isogonal_conjugate(model, A, B, C, X_1804, ID="X_1857", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_4, X_65, 4, 65, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_33, X_42, 33, 42, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    central_line(model, X_2, X_243, 2, 243, incident=True)
    return promote_point_to_top(model, X_1857)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1857 on the given reference triangle."""
    model = create_model('X_1857 = ZOSMA TRANSFORM OF X_223')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01857(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01857.json"))
    write_center_svg(
        model_acute,
        here / "x-01857.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
