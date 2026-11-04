"""GEOMETOR construction model for X_1437 = X_283-BETH CONJUGATE OF X_283."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01437(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1437 = X_283-BETH CONJUGATE OF X_283 on reference triangle ABC."""
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center"])
    X_1437 = cevapoint(model, A, B, C, X_48, X_184, ID="X_1437", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_49 = eval_trilinear_point(model, A, B, C, 'cos(3*A)', ID="X_49", classes=["center", "incident"])
    central_line(model, X_3, X_49, 3, 49, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_60 = eval_trilinear_point(model, A, B, C, '1/(1 + cos(B - C))', ID="X_60", classes=["center", "incident"])
    central_line(model, X_28, X_60, 28, 60, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    central_line(model, X_56, X_58, 56, 58, incident=True)
    return promote_point_to_top(model, X_1437)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1437 on the given reference triangle."""
    model = create_model('X_1437 = X_283-BETH CONJUGATE OF X_283')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01437(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01437.json"))
    write_center_svg(
        model_acute,
        here / "x-01437.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
