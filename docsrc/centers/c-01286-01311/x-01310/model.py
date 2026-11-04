"""GEOMETOR construction model for X_1310 = COLLINGS TRANSFORM OF X_940."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01310(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1310 = COLLINGS TRANSFORM OF X_940 on reference triangle ABC."""
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center"])
    X_940 = eval_trilinear_point(model, A, B, C, '(a**(2) + a*(b + c) + 2*b*c)', ID="X_940", classes=["center"])
    X_1310 = cevapoint(model, A, B, C, X_513, X_940, ID="X_1310", classes=["selected", "target"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_336 = eval_trilinear_point(model, A, B, C, 'csc(A)*cot(A)*sec(A +  omega  )', ID="X_336", classes=["center", "incident"])
    central_line(model, X_98, X_336, 98, 336, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_664 = eval_trilinear_point(model, A, B, C, '1/(a*(b - c)*(b + c - a))', ID="X_664", classes=["center", "incident"])
    central_line(model, X_108, X_664, 108, 664, incident=True)
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    X_662 = eval_trilinear_point(model, A, B, C, '1/(cot(B) - cot(C))', ID="X_662", classes=["center", "incident"])
    central_line(model, X_112, X_662, 112, 662, incident=True)
    return promote_point_to_top(model, X_1310)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1310 on the given reference triangle."""
    model = create_model('X_1310 = COLLINGS TRANSFORM OF X_940')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01310(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01310.json"))
    write_center_svg(
        model_acute,
        here / "x-01310.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
