"""GEOMETOR construction model for X_2356 = X_2-ISOCONJUGATE OF X_1814."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02356(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2356 = X_2-ISOCONJUGATE OF X_1814 on reference triangle ABC."""
    X_1861 = eval_barycentric_point(model, A, B, C, '(b**(2) + c**(2) - a*(b + c))/(a**(2) - b**(2) - c**(2))', ID="X_1861", classes=["center"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center"])
    X_2356 = ceva_conjugate(model, A, B, C, X_1861, X_672, ID="X_2356", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_25, X_41, 25, 41, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_459 = eval_trilinear_point(model, A, B, C, '(sec(A))/(tan(B) + tan(C) - tan(A))', ID="X_459", classes=["center", "incident"])
    central_line(model, X_43, X_459, 43, 459, incident=True)
    return promote_point_to_top(model, X_2356)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2356 on the given reference triangle."""
    model = create_model('X_2356 = X_2-ISOCONJUGATE OF X_1814')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02356(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02356.json"))
    write_center_svg(
        model_acute,
        here / "x-02356.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
