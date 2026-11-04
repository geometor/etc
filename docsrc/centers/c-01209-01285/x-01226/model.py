"""GEOMETOR construction model for X_1226 = ISOTOMIC CONJUGATE OF X_1167."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01226(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1226 = ISOTOMIC CONJUGATE OF X_1167 on reference triangle ABC."""
    X_1167 = point_from_barycentrics(model, A, B, C, 0.35929716, 0.32223282, 0.31847002, ID="X_1167", classes=["center"])
    X_1226 = isotomic_conjugate(model, A, B, C, X_1167, ID="X_1226", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_10, X_75, 10, 75, incident=True)
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center", "incident"])
    central_line(model, X_85, X_264, 85, 264, incident=True)
    X_311 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*cos(B - C)', ID="X_311", classes=["center", "incident"])
    X_349 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C))*(csc(A))**(3)', ID="X_349", classes=["center", "incident"])
    central_line(model, X_311, X_349, 311, 349, incident=True)
    return promote_point_to_top(model, X_1226)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1226 on the given reference triangle."""
    model = create_model('X_1226 = ISOTOMIC CONJUGATE OF X_1167')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01226(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01226.json"))
    write_center_svg(
        model_acute,
        here / "x-01226.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
