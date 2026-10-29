"""GEOMETOR construction model for X(177) = 1st MID-ARC POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00177(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(177) = 1st MID-ARC POINT on reference triangle ABC."""
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X(177)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_167 = point_from_barycentrics(model, A, B, C, 0.58849841, 0.49152493, -0.080023337, ID="X(167)", classes=["center", "incident"])
    central_line(model, X_1, X_167, 1, 167, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X(173)", classes=["center", "incident"])
    central_line(model, X_9, X_173, 9, 173, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X(164)", classes=["center", "incident"])
    central_line(model, X_57, X_164, 57, 164, incident=True)
    return promote_point_to_top(model, X_177)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(177) on the given reference triangle."""
    model = create_model('X(177) = 1st MID-ARC POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00177(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00177.json"))
    write_center_svg(
        model_acute,
        here / "x-00177.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
