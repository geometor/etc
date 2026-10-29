"""GEOMETOR construction model for X(182) = MIDPOINT OF BROCARD DIAMETER."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    midpoint,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00182(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(182) = MIDPOINT OF BROCARD DIAMETER on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_182 = midpoint(model, X_3, X_6, ID="X(182)", classes=["selected", "target"], guide=False)
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X(22)", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    central_line(model, X_22, X_51, 22, 51, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X(83)", classes=["center", "incident"])
    central_line(model, X_4, X_83, 4, 83, incident=True)
    return promote_point_to_top(model, X_182)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(182) on the given reference triangle."""
    model = create_model('X(182) = MIDPOINT OF BROCARD DIAMETER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00182(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00182.json"))
    write_center_svg(
        model_acute,
        here / "x-00182.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
