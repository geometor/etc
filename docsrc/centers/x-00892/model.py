"""GEOMETOR construction model for X(892) = ISOGONAL CONJUGATE OF X(351)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00892(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(892) = ISOGONAL CONJUGATE OF X(351) on reference triangle ABC."""
    X_351 = point_from_barycentrics(model, A, B, C, -1.104798, 0.16783217, 1.9369658, ID="X(351)", classes=["center"])
    X_892 = isogonal_conjugate(model, A, B, C, X_351, ID="X(892)", classes=["selected", "target"])
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X(111)", classes=["center", "incident"])
    X_381 = eval_trilinear_point(model, A, B, C, '2*cos(B - C) - cos(A)', ID="X(381)", classes=["center", "incident"])
    central_line(model, X_111, X_381, 111, 381, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X(523)", classes=["center", "incident"])
    central_line(model, X_99, X_523, 99, 523, incident=True)
    X_316 = point_from_barycentrics(model, A, B, C, 3.0207852, 1.1662818, -3.187067, ID="X(316)", classes=["center", "incident"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X(524)", classes=["center", "incident"])
    central_line(model, X_316, X_524, 316, 524, incident=True)
    return promote_point_to_top(model, X_892)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(892) on the given reference triangle."""
    model = create_model('X(892) = ISOGONAL CONJUGATE OF X(351)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00892(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00892.json"))
    write_center_svg(
        model_acute,
        here / "x-00892.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
