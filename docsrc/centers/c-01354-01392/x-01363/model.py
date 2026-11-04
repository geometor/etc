"""GEOMETOR construction model for X_1363 = BRISSE TRANSFORM OF X_107."""

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


def construct_x_01363(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1363 = BRISSE TRANSFORM OF X_107 on reference triangle ABC."""
    X_1363 = point_from_barycentrics(model, A, B, C, 0.39605447, 0.60045962, 0.0034859063, ID="X_1363", classes=["selected", "target"])
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center", "incident"])
    X_1355 = point_from_barycentrics(model, A, B, C, 0.2130857, 0.031241371, 0.75567293, ID="X_1355", classes=["center", "incident"])
    central_line(model, X_222, X_1355, 222, 1355, incident=True)
    return promote_point_to_top(model, X_1363)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1363 on the given reference triangle."""
    model = create_model('X_1363 = BRISSE TRANSFORM OF X_107')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01363(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01363.json"))
    write_center_svg(
        model_acute,
        here / "x-01363.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
