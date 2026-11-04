"""GEOMETOR construction model for X_1821 = ISOGONAL CONJUGATE OF MIMOSA TRANSFORM OF X_287."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01821(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1821 = ISOGONAL CONJUGATE OF MIMOSA TRANSFORM OF X_287 on reference triangle ABC."""
    X_1755 = eval_trilinear_point(model, A, B, C, 'a*cos(A + omega )', ID="X_1755", classes=["center"])
    X_1821 = isogonal_conjugate(model, A, B, C, X_1755, ID="X_1821", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    central_line(model, X_31, X_92, 31, 92, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_48, X_75, 48, 75, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A + omega )', ID="X_98", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_98, X_100, 98, 100, incident=True)
    return promote_point_to_top(model, X_1821)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1821 on the given reference triangle."""
    model = create_model('X_1821 = ISOGONAL CONJUGATE OF MIMOSA TRANSFORM OF X_287')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01821(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01821.json"))
    write_center_svg(
        model_acute,
        here / "x-01821.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
