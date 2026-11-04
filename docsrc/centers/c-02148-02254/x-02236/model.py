"""GEOMETOR construction model for X_2236 = X_2-ISOCONJUGATE OF X_733."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02236(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2236 = X_2-ISOCONJUGATE OF X_733 on reference triangle ABC."""
    X_1580 = eval_trilinear_point(model, A, B, C, 'a**(4) - b**(2)*c**(2)', ID="X_1580", classes=["center"])
    X_1966 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(a**(4) - b**(2)*c**(2))', ID="X_1966", classes=["center"])
    X_2236 = crosspoint(model, A, B, C, X_1580, X_1966, ID="X_2236", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_31, X_75, 31, 75, incident=True)
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    X_385 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) - b**(2)*c**(2))', ID="X_385", classes=["center", "incident"])
    central_line(model, X_171, X_385, 171, 385, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    return promote_point_to_top(model, X_2236)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2236 on the given reference triangle."""
    model = create_model('X_2236 = X_2-ISOCONJUGATE OF X_733')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02236(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02236.json"))
    write_center_svg(
        model_acute,
        here / "x-02236.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
