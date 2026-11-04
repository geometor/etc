"""GEOMETOR construction model for X_1394 = X_20-BETH CONJUGATE OF X_20."""

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
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01394(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1394 = X_20-BETH CONJUGATE OF X_20 on reference triangle ABC."""
    X_221 = eval_trilinear_point(model, A, B, C, '((sin(A/2))**(2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_221", classes=["center"])
    X_1035 = point_from_barycentrics(model, A, B, C, 9.6083789, 14.775956, -23.384335, ID="X_1035", classes=["center"])
    X_1394 = cevapoint(model, A, B, C, X_221, X_1035, ID="X_1394", classes=["selected", "target"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_28, X_34, 28, 34, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center", "incident"])
    central_line(model, X_1, X_84, 1, 84, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_21, X_77, 21, 77, incident=True)
    return promote_point_to_top(model, X_1394)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1394 on the given reference triangle."""
    model = create_model('X_1394 = X_20-BETH CONJUGATE OF X_20')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01394(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01394.json"))
    write_center_svg(
        model_acute,
        here / "x-01394.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
