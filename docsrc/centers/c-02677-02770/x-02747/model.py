"""GEOMETOR construction model for X_2747 = SR(X_104, X_112)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02747(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2747 = SR(X_104, X_112) on reference triangle ABC."""
    X_2722 = point_from_barycentrics(model, A, B, C, -0.17330373, 0.51887137, 0.65443236, ID="X_2722", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2747 = reflection_in_point(model, X_2722, X_3, ID="X_2747", classes=["selected", "target"], guide=False)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_104, X_525, 104, 525, incident=True)
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_112, X_517, 112, 517, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_1503 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(omega)  - 2*cos(B)*cos(C)', ID="X_1503", classes=["center", "incident"])
    central_line(model, X_100, X_1503, 100, 1503, incident=True)
    return promote_point_to_top(model, X_2747)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2747 on the given reference triangle."""
    model = create_model('X_2747 = SR(X_104, X_112)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02747(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02747.json"))
    write_center_svg(
        model_acute,
        here / "x-02747.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
