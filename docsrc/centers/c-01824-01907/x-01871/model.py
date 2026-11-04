"""GEOMETOR construction model for X_1871 = ZOSMA TRANSFORM OF X_498."""

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
    intersect_lines,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01871(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1871 = ZOSMA TRANSFORM OF X_498 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    central_line(model, X_4, X_8, 4, 8)
    central_line(model, X_3, X_19, 3, 19)
    X_1871 = intersect_lines(model, X_4, X_8, X_3, X_19, ID="X_1871", classes=["selected", "target"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    X_392 = eval_trilinear_point(model, A, B, C, '(b + c)*(b**(2) + c**(2) - a**(2)) + 4*a*b*c', ID="X_392", classes=["center", "incident"])
    central_line(model, X_29, X_392, 29, 392, incident=True)
    return promote_point_to_top(model, X_1871)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1871 on the given reference triangle."""
    model = create_model('X_1871 = ZOSMA TRANSFORM OF X_498')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01871(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01871.json"))
    write_center_svg(
        model_acute,
        here / "x-01871.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
