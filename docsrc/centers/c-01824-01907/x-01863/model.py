"""GEOMETOR construction model for X_1863 = ZOSMA TRANSFORM OF X_269."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01863(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1863 = ZOSMA TRANSFORM OF X_269 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1851 = point_from_barycentrics(model, A, B, C, 0.076660459, 0.18621974, 0.7371198, ID="X_1851", classes=["center"])
    X_1863 = ceva_conjugate(model, A, B, C, X_4, X_1851, ID="X_1863", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_4, X_7, 4, 7, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_33, X_42, 33, 42, incident=True)
    X_242 = eval_trilinear_point(model, A, B, C, '((sec(A))*((sin(A))**(2) - sin(B)*sin(C)))', ID="X_242", classes=["center", "incident"])
    X_390 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(3*a**(2) + (b - c)**(2))', ID="X_390", classes=["center", "incident"])
    central_line(model, X_242, X_390, 242, 390, incident=True)
    return promote_point_to_top(model, X_1863)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1863 on the given reference triangle."""
    model = create_model('X_1863 = ZOSMA TRANSFORM OF X_269')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01863(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01863.json"))
    write_center_svg(
        model_acute,
        here / "x-01863.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
