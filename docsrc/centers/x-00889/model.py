"""GEOMETOR construction model for X(889) = INTERSECTION OF LINES X(99)X(898) AND X(190)X(649)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00889(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(889) = INTERSECTION OF LINES X(99)X(898) AND X(190)X(649) on reference triangle ABC."""
    X_889 = eval_barycentric_point(model, A, B, C, 'b*c/((b - c)*(a*b + a*c - 2*b*c))', ID="X(889)", classes=["selected", "target"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X(649)", classes=["center", "incident"])
    central_line(model, X_190, X_649, 190, 649, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    X_668 = eval_trilinear_point(model, A, B, C, '1/(a**(2)*(b - c))', ID="X(668)", classes=["center", "incident"])
    central_line(model, X_513, X_668, 513, 668, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    X_898 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(2*b*c - a*b - a*c))', ID="X(898)", classes=["center", "incident"])
    central_line(model, X_99, X_898, 99, 898, incident=True)
    return promote_point_to_top(model, X_889)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(889) on the given reference triangle."""
    model = create_model('X(889) = INTERSECTION OF LINES X(99)X(898) AND X(190)X(649)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00889(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00889.json"))
    write_center_svg(
        model_acute,
        here / "x-00889.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
