"""GEOMETOR construction model for X_2572 = INSIMILICENTER(BEVAN, 2nd BROCARD CIRCLE)."""

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
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02572(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2572 = INSIMILICENTER(BEVAN, 2nd BROCARD CIRCLE) on reference triangle ABC."""
    X_2572 = eval_trilinear_point(model, A, B, C, '(1 - cos(B) - cos(C) + (1 + 2/e)*cos(A))', ID="X_2572", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_2569 = eval_trilinear_point(model, A, B, C, '(b*c*((b + c)*e - a*cos(A)))', ID="X_2569", classes=["center", "incident"])
    central_line(model, X_9, X_2569, 9, 2569, incident=True)
    X_1342 = eval_trilinear_point(model, A, B, C, 'sin(A) + cos(A)*cot( omega  /2)', ID="X_1342", classes=["center", "incident"])
    X_1705 = eval_trilinear_point(model, A, B, C, '(2*cos(A -  omega  ) - e*(1 + cos(A) - cos(B) - cos(C)))', ID="X_1705", classes=["center", "incident"])
    central_line(model, X_1342, X_1705, 1342, 1705, incident=True)
    return promote_point_to_top(model, X_2572)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2572 on the given reference triangle."""
    model = create_model('X_2572 = INSIMILICENTER(BEVAN, 2nd BROCARD CIRCLE)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02572(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02572.json"))
    write_center_svg(
        model_acute,
        here / "x-02572.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
