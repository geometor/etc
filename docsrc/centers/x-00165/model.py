"""GEOMETOR construction model for X(165) = CENTROID OF THE EXCENTRAL TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00165(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(165) = CENTROID OF THE EXCENTRAL TRIANGLE on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_165 = ceva_conjugate(model, A, B, C, X_9, X_1, ID="X(165)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X(20)", classes=["center", "incident"])
    central_line(model, X_10, X_20, 10, 20, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X(63)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_63, X_100, 63, 100, incident=True)
    return promote_point_to_top(model, X_165)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(165) on the given reference triangle."""
    model = create_model('X(165) = CENTROID OF THE EXCENTRAL TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00165(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00165.json"))
    write_center_svg(
        model_acute,
        here / "x-00165.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
