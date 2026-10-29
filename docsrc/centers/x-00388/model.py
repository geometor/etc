"""GEOMETOR construction model for X(388) = X(1)X(4)∩X(7)X(8)."""

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
    incenter_of,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00388(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(388) = X(1)X(4)∩X(7)X(8) on reference triangle ABC."""
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X(388)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X(12)", classes=["center", "incident"])
    central_line(model, X_2, X_12, 2, 12, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    central_line(model, X_7, X_8, 7, 8, incident=True)
    return promote_point_to_top(model, X_388)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(388) on the given reference triangle."""
    model = create_model('X(388) = X(1)X(4)∩X(7)X(8)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00388(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00388.json"))
    write_center_svg(
        model_acute,
        here / "x-00388.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
