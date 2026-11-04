"""GEOMETOR construction model for X_2142 = EIGENTRANSFORM OF X_512."""

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


def construct_x_02142(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2142 = EIGENTRANSFORM OF X_512 on reference triangle ABC."""
    X_2142 = point_from_barycentrics(model, A, B, C, 0.26100517, 2.5501505, -1.8111556, ID="X_2142", classes=["selected", "target"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_2143 = point_from_barycentrics(model, A, B, C, 1.1561664, 0.17039865, -0.3265651, ID="X_2143", classes=["center", "incident"])
    central_line(model, X_512, X_2143, 512, 2143, incident=True)
    return promote_point_to_top(model, X_2142)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2142 on the given reference triangle."""
    model = create_model('X_2142 = EIGENTRANSFORM OF X_512')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02142(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02142.json"))
    write_center_svg(
        model_acute,
        here / "x-02142.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
