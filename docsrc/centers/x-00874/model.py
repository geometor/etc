"""GEOMETOR construction model for X(874) = INTERSECTION OF LINES X(1)X(75) AND X(99)X(670)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00874(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(874) = INTERSECTION OF LINES X(1)X(75) AND X(99)X(670) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center"])
    X_670 = eval_trilinear_point(model, A, B, C, '1/(a**(3)*(b**(2) - c**(2)))', ID="X(670)", classes=["center"])
    central_line(model, X_1, X_75, 1, 75)
    central_line(model, X_99, X_670, 99, 670)
    X_874 = intersect_lines(model, X_1, X_75, X_99, X_670, ID="X(874)", classes=["selected", "target"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    X_646 = point_from_barycentrics(model, A, B, C, 0.95726496, -0.2991453, 0.34188034, ID="X(646)", classes=["center", "incident"])
    central_line(model, X_190, X_646, 190, 646, incident=True)
    return promote_point_to_top(model, X_874)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(874) on the given reference triangle."""
    model = create_model('X(874) = INTERSECTION OF LINES X(1)X(75) AND X(99)X(670)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00874(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00874.json"))
    write_center_svg(
        model_acute,
        here / "x-00874.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
