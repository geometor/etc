"""GEOMETOR construction model for X(835) = o-(2, 3) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00835(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(835) = o-(2, 3) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_834 = point_from_barycentrics(model, A, B, C, -0.29731832, 0.80721923, -0.50990091, ID="X(834)", classes=["center"])
    X_835 = isogonal_conjugate(model, A, B, C, X_834, ID="X(835)", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    central_line(model, X_110, X_190, 110, 190, incident=True)
    X_335 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(2) - b*c)', ID="X(335)", classes=["center", "incident"])
    X_741 = point_from_barycentrics(model, A, B, C, -0.036241685, 0.96112949, 0.075112193, ID="X(741)", classes=["center", "incident"])
    central_line(model, X_335, X_741, 335, 741, incident=True)
    return promote_point_to_top(model, X_835)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(835) on the given reference triangle."""
    model = create_model('X(835) = o-(2, 3) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00835(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00835.json"))
    write_center_svg(
        model_acute,
        here / "x-00835.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
