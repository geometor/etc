"""GEOMETOR construction model for X(858) = COMPLEMENT OF X(23)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00858(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(858) = COMPLEMENT OF X(23) on reference triangle ABC."""
    X_23 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(23)", classes=["center"])
    X_858 = complement(model, A, B, C, X_23, ID="X(858)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X(50)", classes=["center", "incident"])
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X(230)", classes=["center", "incident"])
    central_line(model, X_50, X_230, 50, 230, incident=True)
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X(67)", classes=["center", "incident"])
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X(524)", classes=["center", "incident"])
    central_line(model, X_67, X_524, 67, 524, incident=True)
    return promote_point_to_top(model, X_858)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(858) on the given reference triangle."""
    model = create_model('X(858) = COMPLEMENT OF X(23)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00858(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00858.json"))
    write_center_svg(
        model_acute,
        here / "x-00858.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
