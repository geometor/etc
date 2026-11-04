"""GEOMETOR construction model for X_1582 = POINT CANOPUS."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01582(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1582 = POINT CANOPUS on reference triangle ABC."""
    X_1582 = eval_trilinear_point(model, A, B, C, 'a**(4) + b**(2)*c**(2)', ID="X_1582", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_1, X_19, 1, 19, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    central_line(model, X_6, X_291, 6, 291, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X_560", classes=["center", "incident"])
    central_line(model, X_75, X_560, 75, 560, incident=True)
    return promote_point_to_top(model, X_1582)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1582 on the given reference triangle."""
    model = create_model('X_1582 = POINT CANOPUS')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01582(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01582.json"))
    write_center_svg(
        model_acute,
        here / "x-01582.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
