"""GEOMETOR construction model for X(563) = TRILINEAR PRODUCT X(47)*X(48)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00563(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(563) = TRILINEAR PRODUCT X(47)*X(48) on reference triangle ABC."""
    X_563 = eval_trilinear_point(model, A, B, C, 'sin(4*A)', ID="X(563)", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X(163)", classes=["center", "incident"])
    central_line(model, X_19, X_163, 19, 163, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '1 + cos(2*A)', ID="X(255)", classes=["center", "incident"])
    central_line(model, X_48, X_255, 48, 255, incident=True)
    return promote_point_to_top(model, X_563)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(563) on the given reference triangle."""
    model = create_model('X(563) = TRILINEAR PRODUCT X(47)*X(48)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00563(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00563.json"))
    write_center_svg(
        model_acute,
        here / "x-00563.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
