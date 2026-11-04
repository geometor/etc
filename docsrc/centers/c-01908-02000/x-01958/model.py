"""GEOMETOR construction model for X_1958 = CROSSSUM OF PU(23)."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01958(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1958 = CROSSSUM OF PU(23) on reference triangle ABC."""
    X_610 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C) - tan(A)', ID="X_610", classes=["center"])
    X_1740 = eval_trilinear_point(model, A, B, C, '(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_1740", classes=["center"])
    X_1958 = cevapoint(model, A, B, C, X_610, X_1740, ID="X_1958", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_48, X_75, 48, 75, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_326 = eval_trilinear_point(model, A, B, C, '(cot(A))**(2)', ID="X_326", classes=["center", "incident"])
    central_line(model, X_19, X_326, 19, 326, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_63, X_610, 63, 610, incident=True)
    return promote_point_to_top(model, X_1958)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1958 on the given reference triangle."""
    model = create_model('X_1958 = CROSSSUM OF PU(23)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01958(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01958.json"))
    write_center_svg(
        model_acute,
        here / "x-01958.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
