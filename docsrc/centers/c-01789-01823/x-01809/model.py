"""GEOMETOR construction model for X_1809 = INVERSE MIMOSA TRANSFORM OF X_515."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01809(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1809 = INVERSE MIMOSA TRANSFORM OF X_515 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center"])
    central_line(model, X_3, X_8, 3, 8)
    central_line(model, X_78, X_255, 78, 255)
    X_1809 = intersect_lines(model, X_3, X_8, X_78, X_255, ID="X_1809", classes=["selected", "target"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_1804 = eval_trilinear_point(model, A, B, C, '(1 + cos(2*A))/(1 + cos(A))', ID="X_1804", classes=["center", "incident"])
    central_line(model, X_69, X_1804, 69, 1804, incident=True)
    return promote_point_to_top(model, X_1809)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1809 on the given reference triangle."""
    model = create_model('X_1809 = INVERSE MIMOSA TRANSFORM OF X_515')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01809(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01809.json"))
    write_center_svg(
        model_acute,
        here / "x-01809.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
