"""GEOMETOR construction model for X_2348 = X_2-ISOCONJUGATE OF X_1477."""

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
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02348(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2348 = X_2-ISOCONJUGATE OF X_1477 on reference triangle ABC."""
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_2348 = ceva_conjugate(model, A, B, C, X_105, X_55, ID="X_2348", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_9, X_55, 9, 55, incident=True)
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    X_169 = eval_trilinear_point(model, A, B, C, '- (sin(A))*(cos(A/2))**(2) + (sin(B))*(cos(B/2))**(2) + (sin(C))*(cos(C/2))**(2)', ID="X_169", classes=["center", "incident"])
    central_line(model, X_65, X_169, 65, 169, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_354 = eval_trilinear_point(model, A, B, C, '(b - c)**(2) - a*b - a*c', ID="X_354", classes=["center", "incident"])
    central_line(model, X_6, X_354, 6, 354, incident=True)
    return promote_point_to_top(model, X_2348)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2348 on the given reference triangle."""
    model = create_model('X_2348 = X_2-ISOCONJUGATE OF X_1477')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02348(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02348.json"))
    write_center_svg(
        model_acute,
        here / "x-02348.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
