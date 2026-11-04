"""GEOMETOR construction model for X_1435 = X_278-BETH CONJUGATE OF X_278."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01435(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1435 = X_278-BETH CONJUGATE OF X_278 on reference triangle ABC."""
    X_608 = eval_trilinear_point(model, A, B, C, 'a*(1 - sec(A))', ID="X_608", classes=["center"])
    X_1398 = point_from_barycentrics(model, A, B, C, 0.022602903, 0.091363312, 0.88603379, ID="X_1398", classes=["center"])
    X_1435 = cevapoint(model, A, B, C, X_608, X_1398, ID="X_1435", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_25, X_34, 25, 34, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_19, X_57, 19, 57, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    central_line(model, X_48, X_223, 48, 223, incident=True)
    return promote_point_to_top(model, X_1435)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1435 on the given reference triangle."""
    model = create_model('X_1435 = X_278-BETH CONJUGATE OF X_278')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01435(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01435.json"))
    write_center_svg(
        model_acute,
        here / "x-01435.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
