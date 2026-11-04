"""GEOMETOR construction model for X_1422 = X_189-BETH CONJUGATE OF X_189."""

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
    incenter_of,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01422(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1422 = X_189-BETH CONJUGATE OF X_189 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X_84", classes=["center"])
    central_line(model, X_2, X_77, 2, 77)
    central_line(model, X_1, X_84, 1, 84)
    X_1422 = intersect_lines(model, X_2, X_77, X_1, X_84, ID="X_1422", classes=["selected", "target"])
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center", "incident"])
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center", "incident"])
    central_line(model, X_269, X_278, 269, 278, incident=True)
    return promote_point_to_top(model, X_1422)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1422 on the given reference triangle."""
    model = create_model('X_1422 = X_189-BETH CONJUGATE OF X_189')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01422(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01422.json"))
    write_center_svg(
        model_acute,
        here / "x-01422.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
