"""GEOMETOR construction model for X(982) = INTERSECTION OF LINES X(1)X(3) AND X(2)X(38)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00982(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(982) = INTERSECTION OF LINES X(1)X(3) AND X(2)X(38) on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X(38)", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_2, X_38, 2, 38)
    X_982 = intersect_lines(model, X_1, X_3, X_2, X_38, ID="X(982)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X(256)", classes=["center", "incident"])
    central_line(model, X_7, X_256, 7, 256, incident=True)
    return promote_point_to_top(model, X_982)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(982) on the given reference triangle."""
    model = create_model('X(982) = INTERSECTION OF LINES X(1)X(3) AND X(2)X(38)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00982(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00982.json"))
    write_center_svg(
        model_acute,
        here / "x-00982.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
