"""GEOMETOR construction model for X_1107 = CROSSPOINT OF X_1 AND X_274."""

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
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01107(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1107 = CROSSPOINT OF X_1 AND X_274 on reference triangle ABC."""
    X_1107 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2)) + b*c*(b + c))', ID="X_1107", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_10, X_39, 10, 39, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    central_line(model, X_75, X_194, 75, 194, incident=True)
    return promote_point_to_top(model, X_1107)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1107 on the given reference triangle."""
    model = create_model('X_1107 = CROSSPOINT OF X_1 AND X_274')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01107(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01107.json"))
    write_center_svg(
        model_acute,
        here / "x-01107.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
