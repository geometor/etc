"""GEOMETOR construction model for X(136) = INTERSECTION OF LINE X(4)X(110) AND X(25)X(132)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nine_point_center_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00136(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(136) = INTERSECTION OF LINE X(4)X(110) AND X(25)X(132) on reference triangle ABC."""
    X_131 = point_from_barycentrics(model, A, B, C, 0.57236082, 0.12379803, 0.30384114, ID="X(131)", classes=["center"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center"])
    X_136 = reflection_in_point(model, X_131, X_5, ID="X(136)", classes=["selected", "target"], guide=False)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    central_line(model, X_4, X_110, 4, 110, incident=True)
    central_line(model, X_5, X_131, 5, 131, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X(132)", classes=["center", "incident"])
    central_line(model, X_25, X_132, 25, 132, incident=True)
    return promote_point_to_top(model, X_136)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(136) on the given reference triangle."""
    model = create_model('X(136) = INTERSECTION OF LINE X(4)X(110) AND X(25)X(132)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00136(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00136.json"))
    write_center_svg(
        model_acute,
        here / "x-00136.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
