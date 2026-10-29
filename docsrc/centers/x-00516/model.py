"""GEOMETOR construction model for X(516) = ISOGONAL CONJUGATE OF X(103)."""

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
    gergonne_point_of,
    incenter_of,
    isogonal_conjugate,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00516(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(516) = ISOGONAL CONJUGATE OF X(103) on reference triangle ABC."""
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X(103)", classes=["center"])
    X_516 = isogonal_conjugate(model, A, B, C, X_103, ID="X(516)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X(142)", classes=["center", "incident"])
    central_line(model, X_3, X_142, 3, 142, incident=True)
    return promote_point_to_top(model, X_516)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(516) on the given reference triangle."""
    model = create_model('X(516) = ISOGONAL CONJUGATE OF X(103)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00516(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00516.json"))
    write_center_svg(
        model_acute,
        here / "x-00516.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
