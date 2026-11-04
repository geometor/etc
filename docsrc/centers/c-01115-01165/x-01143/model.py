"""GEOMETOR construction model for X_1143 = 2nd MALFATTI-RABINOWITZ POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01143(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1143 = 2nd MALFATTI-RABINOWITZ POINT on reference triangle ABC."""
    X_1143 = eval_trilinear_point(model, A, B, C, 'csc(A)*tan(A/4)', ID="X_1143", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X_177", classes=["center", "incident"])
    central_line(model, X_8, X_177, 8, 177, incident=True)
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X_174", classes=["center", "incident"])
    X_175 = eval_trilinear_point(model, A, B, C, '-1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X_175", classes=["center", "incident"])
    central_line(model, X_174, X_175, 174, 175, incident=True)
    X_558 = eval_trilinear_point(model, A, B, C, 'sec(A/2)*tan(A/4)', ID="X_558", classes=["center", "incident"])
    X_1488 = eval_trilinear_point(model, A, B, C, '1/(1 + sin(A/2))', ID="X_1488", classes=["center", "incident"])
    central_line(model, X_558, X_1488, 558, 1488, incident=True)
    return promote_point_to_top(model, X_1143)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1143 on the given reference triangle."""
    model = create_model('X_1143 = 2nd MALFATTI-RABINOWITZ POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01143(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01143.json"))
    write_center_svg(
        model_acute,
        here / "x-01143.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
