"""GEOMETOR construction model for X_2085 = NK-TRANSFORM OF X_31."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02085(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2085 = NK-TRANSFORM OF X_31 on reference triangle ABC."""
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_2085 = crosspoint(model, A, B, C, X_31, X_75, ID="X_2085", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1581 = eval_trilinear_point(model, A, B, C, '1/(a**(4) - b**(2)*c**(2))', ID="X_1581", classes=["center", "incident"])
    central_line(model, X_1, X_1581, 1, 1581, incident=True)
    X_1917 = eval_trilinear_point(model, A, B, C, 'a**(6)', ID="X_1917", classes=["center", "incident"])
    central_line(model, X_31, X_1917, 31, 1917, incident=True)
    X_1928 = eval_trilinear_point(model, A, B, C, '1/a**(6)', ID="X_1928", classes=["center", "incident"])
    central_line(model, X_75, X_1928, 75, 1928, incident=True)
    return promote_point_to_top(model, X_2085)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2085 on the given reference triangle."""
    model = create_model('X_2085 = NK-TRANSFORM OF X_31')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02085(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02085.json"))
    write_center_svg(
        model_acute,
        here / "x-02085.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
