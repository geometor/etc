"""GEOMETOR construction model for X(922) = POINT ALBALI."""

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


def construct_x_00922(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(922) = POINT ALBALI on reference triangle ABC."""
    X_922 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(2) + c**(2) - 2*a**(2))', ID="X(922)", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    central_line(model, X_31, X_48, 31, 48, incident=True)
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X(667)", classes=["center", "incident"])
    X_788 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b**(3) - c**(3))', ID="X(788)", classes=["center", "incident"])
    central_line(model, X_667, X_788, 667, 788, incident=True)
    return promote_point_to_top(model, X_922)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(922) on the given reference triangle."""
    model = create_model('X(922) = POINT ALBALI')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00922(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00922.json"))
    write_center_svg(
        model_acute,
        here / "x-00922.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
