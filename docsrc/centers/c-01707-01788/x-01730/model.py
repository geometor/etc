"""GEOMETOR construction model for X_1730 = MIMOSA TRANSFORM OF X_86."""

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
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01730(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1730 = MIMOSA TRANSFORM OF X_86 on reference triangle ABC."""
    X_286 = eval_trilinear_point(model, A, B, C, '(csc(2*A))/(sin(B) + sin(C))', ID="X_286", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1730 = ceva_conjugate(model, A, B, C, X_286, X_1, ID="X_1730", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_6, X_57, 6, 57, incident=True)
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["center", "incident"])
    central_line(model, X_1, X_228, 1, 228, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_169 = eval_trilinear_point(model, A, B, C, '- (sin(A))*(cos(A/2))**(2) + (sin(B))*(cos(B/2))**(2) + (sin(C))*(cos(C/2))**(2)', ID="X_169", classes=["center", "incident"])
    central_line(model, X_63, X_169, 63, 169, incident=True)
    return promote_point_to_top(model, X_1730)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1730 on the given reference triangle."""
    model = create_model('X_1730 = MIMOSA TRANSFORM OF X_86')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01730(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01730.json"))
    write_center_svg(
        model_acute,
        here / "x-01730.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
