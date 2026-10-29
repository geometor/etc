"""GEOMETOR construction model for X(893) = X(238)-CROSS CONJUGATE OF X(292)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00893(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(893) = X(238)-CROSS CONJUGATE OF X(292) on reference triangle ABC."""
    X_893 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) + b*c)', ID="X(893)", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center", "incident"])
    central_line(model, X_9, X_43, 9, 43, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A + omega )', ID="X(232)", classes=["center", "incident"])
    central_line(model, X_19, X_232, 19, 232, incident=True)
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X(171)", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X(292)", classes=["center", "incident"])
    central_line(model, X_171, X_292, 171, 292, incident=True)
    return promote_point_to_top(model, X_893)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(893) on the given reference triangle."""
    model = create_model('X(893) = X(238)-CROSS CONJUGATE OF X(292)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00893(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00893.json"))
    write_center_svg(
        model_acute,
        here / "x-00893.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
