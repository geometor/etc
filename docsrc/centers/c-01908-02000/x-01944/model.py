"""GEOMETOR construction model for X_1944 = CROSSDIFFERENCE OF PU(18)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01944(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1944 = CROSSDIFFERENCE OF PU(18) on reference triangle ABC."""
    X_1944 = eval_trilinear_point(model, A, B, C, '(b*c*((cos(A))**(2) - cos(B)*cos(C)))', ID="X_1944", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_2, X_7, 2, 7, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center", "incident"])
    central_line(model, X_75, X_219, 75, 219, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_281 = eval_trilinear_point(model, A, B, C, 'sec(A)*cot(A/2)', ID="X_281", classes=["center", "incident"])
    central_line(model, X_69, X_281, 69, 281, incident=True)
    return promote_point_to_top(model, X_1944)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1944 on the given reference triangle."""
    model = create_model('X_1944 = CROSSDIFFERENCE OF PU(18)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01944(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01944.json"))
    write_center_svg(
        model_acute,
        here / "x-01944.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
