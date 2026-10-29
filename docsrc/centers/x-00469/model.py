"""GEOMETOR construction model for X(469) = EULER LINE INTERCEPT OF LINE X(92)X(264)."""

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
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00469(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(469) = EULER LINE INTERCEPT OF LINE X(92)X(264) on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X(264)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_92, X_264, 92, 264)
    X_469 = intersect_lines(model, X_2, X_3, X_92, X_264, ID="X(469)", classes=["selected", "target"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X(226)", classes=["center", "incident"])
    X_273 = eval_trilinear_point(model, A, B, C, 'sec(A)*(sec(A/2))**(2)', ID="X(273)", classes=["center", "incident"])
    central_line(model, X_226, X_273, 226, 273, incident=True)
    return promote_point_to_top(model, X_469)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(469) on the given reference triangle."""
    model = create_model('X(469) = EULER LINE INTERCEPT OF LINE X(92)X(264)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00469(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00469.json"))
    write_center_svg(
        model_acute,
        here / "x-00469.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
