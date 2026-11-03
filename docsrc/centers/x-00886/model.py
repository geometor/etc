"""GEOMETOR construction model for X_886 = INTERSECTION OF LINES X_99X_669 AND X_512X_670."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00886(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_886 = INTERSECTION OF LINES X_99X_669 AND X_512X_670 on reference triangle ABC."""
    X_886 = eval_barycentric_point(model, A, B, C, 'b**(2)*c**(2)/((b**(2) - c**(2))*(a**(2)*b**(2) + a**(2)*c**(2) - 2*b**(2)*c**(2)))', ID="X_886", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X_669", classes=["center", "incident"])
    central_line(model, X_99, X_669, 99, 669, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_670 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(2) - c**(2)))', ID="X_670", classes=["center", "incident"])
    central_line(model, X_512, X_670, 512, 670, incident=True)
    X_880 = point_from_barycentrics(model, A, B, C, 4.3698192, 0.10246315, -3.4722823, ID="X_880", classes=["center", "incident"])
    X_892 = point_from_barycentrics(model, A, B, C, 0.18830409, 0.44770721, 0.3639887, ID="X_892", classes=["center", "incident"])
    central_line(model, X_880, X_892, 880, 892, incident=True)
    return promote_point_to_top(model, X_886)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_886 on the given reference triangle."""
    model = create_model('X_886 = INTERSECTION OF LINES X_99X_669 AND X_512X_670')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00886(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00886.json"))
    write_center_svg(
        model_acute,
        here / "x-00886.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
