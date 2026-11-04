"""GEOMETOR construction model for X_1517 = ORTHOJOIN OF X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01517(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1517 = ORTHOJOIN OF X_7 on reference triangle ABC."""
    X_1517 = point_from_barycentrics(model, A, B, C, -0.174178, 10.861395, -9.6872166, ID="X_1517", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_218 = eval_trilinear_point(model, A, B, C, '((cos(A/2))**(2)*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4)))', ID="X_218", classes=["center", "incident"])
    central_line(model, X_4, X_218, 4, 218, incident=True)
    return promote_point_to_top(model, X_1517)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1517 on the given reference triangle."""
    model = create_model('X_1517 = ORTHOJOIN OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01517(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01517.json"))
    write_center_svg(
        model_acute,
        here / "x-01517.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
