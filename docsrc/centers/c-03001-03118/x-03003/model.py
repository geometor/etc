"""GEOMETOR construction model for X_3003 = (BROCARD AXIS)∩(ORTHIC AXIS)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03003(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3003 = (BROCARD AXIS)∩(ORTHIC AXIS) on reference triangle ABC."""
    X_2986 = eval_barycentric_point(model, A, B, C, '1/(1 + cos(2*B) + cos(2*C))', ID="X_2986", classes=["center"])
    X_3003 = isogonal_conjugate(model, A, B, C, X_2986, ID="X_3003", classes=["selected", "target"])
    return promote_point_to_top(model, X_3003)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3003 on the given reference triangle."""
    model = create_model('X_3003 = (BROCARD AXIS)∩(ORTHIC AXIS)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03003(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03003.json"))
    write_center_svg(
        model_acute,
        here / "x-03003.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
