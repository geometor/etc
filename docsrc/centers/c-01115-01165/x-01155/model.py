"""GEOMETOR construction model for X_1155 = SCHRÖDER POINT."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01155(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1155 = SCHRÖDER POINT on reference triangle ABC."""
    X_1155 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C) - 2*cos(A))', ID="X_1155", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_88, X_105, 88, 105, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    central_line(model, X_63, X_210, 63, 210, incident=True)
    return promote_point_to_top(model, X_1155)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1155 on the given reference triangle."""
    model = create_model('X_1155 = SCHRÖDER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01155(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01155.json"))
    write_center_svg(
        model_acute,
        here / "x-01155.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
