"""GEOMETOR construction model for X_1762 = MIMOSA TRANSFORM OF X_307."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01762(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1762 = MIMOSA TRANSFORM OF X_307 on reference triangle ABC."""
    X_1441 = eval_barycentric_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_1441", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1762 = ceva_conjugate(model, A, B, C, X_1441, X_1, ID="X_1762", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    central_line(model, X_19, X_27, 19, 27, incident=True)
    X_30 = eval_trilinear_point(model, A, B, C, 'cos(A) - 2*cos(B)*cos(C)', ID="X_30", classes=["center", "incident"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    central_line(model, X_30, X_40, 30, 40, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_440 = point_from_barycentrics(model, A, B, C, 0.44199278, 0.40077713, 0.15723009, ID="X_440", classes=["center", "incident"])
    central_line(model, X_9, X_440, 9, 440, incident=True)
    return promote_point_to_top(model, X_1762)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1762 on the given reference triangle."""
    model = create_model('X_1762 = MIMOSA TRANSFORM OF X_307')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01762(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01762.json"))
    write_center_svg(
        model_acute,
        here / "x-01762.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
