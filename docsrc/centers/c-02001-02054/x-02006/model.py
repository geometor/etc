"""GEOMETOR construction model for X_2006 = ORTHOCORRESPONDENT OF X_80."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02006(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2006 = ORTHOCORRESPONDENT OF X_80 on reference triangle ABC."""
    X_2006 = eval_trilinear_point(model, A, B, C, 'sin(A/2)*sec(3*A/2)', ID="X_2006", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_89 = eval_trilinear_point(model, A, B, C, '1/(2*b + 2*c - a)', ID="X_89", classes=["center", "incident"])
    central_line(model, X_7, X_89, 7, 89, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    central_line(model, X_28, X_108, 28, 108, incident=True)
    return promote_point_to_top(model, X_2006)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2006 on the given reference triangle."""
    model = create_model('X_2006 = ORTHOCORRESPONDENT OF X_80')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02006(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02006.json"))
    write_center_svg(
        model_acute,
        here / "x-02006.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
