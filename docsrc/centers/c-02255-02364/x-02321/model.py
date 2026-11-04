"""GEOMETOR construction model for X_2321 = X_2-ISOCONJUGATE OF X_1408."""

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
    mittenpunkt_of,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02321(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2321 = X_2-ISOCONJUGATE OF X_1408 on reference triangle ABC."""
    X_1412 = eval_trilinear_point(model, A, B, C, 'a/((b + c)*(a - b - c))', ID="X_1412", classes=["center"])
    X_2321 = isogonal_conjugate(model, A, B, C, X_1412, ID="X_2321", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_8, X_9, 8, 9, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_10, X_37, 10, 37, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    central_line(model, X_75, X_142, 75, 142, incident=True)
    return promote_point_to_top(model, X_2321)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2321 on the given reference triangle."""
    model = create_model('X_2321 = X_2-ISOCONJUGATE OF X_1408')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02321(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02321.json"))
    write_center_svg(
        model_acute,
        here / "x-02321.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
