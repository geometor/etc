"""GEOMETOR construction model for X_2417 = GIBERT-SIMSON TRANSFORM OF X_1295."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02417(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2417 = GIBERT-SIMSON TRANSFORM OF X_1295 on reference triangle ABC."""
    X_2417 = point_from_barycentrics(model, A, B, C, 16.836502, -14.809886, -1.026616, ID="X_2417", classes=["selected", "target"])
    X_1812 = eval_trilinear_point(model, A, B, C, 'cot(A)*cot(A/2)/(b + c)', ID="X_1812", classes=["center", "incident"])
    X_2431 = point_from_barycentrics(model, A, B, C, -2.5894737, 3.28, 0.30947368, ID="X_2431", classes=["center", "incident"])
    central_line(model, X_1812, X_2431, 1812, 2431, incident=True)
    return promote_point_to_top(model, X_2417)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2417 on the given reference triangle."""
    model = create_model('X_2417 = GIBERT-SIMSON TRANSFORM OF X_1295')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02417(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02417.json"))
    write_center_svg(
        model_acute,
        here / "x-02417.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
