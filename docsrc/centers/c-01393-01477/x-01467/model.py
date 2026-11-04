"""GEOMETOR construction model for X_1467 = X_938-BETH CONJUGATE OF X_938."""

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
    gergonne_point_of,
    incenter_of,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01467(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1467 = X_938-BETH CONJUGATE OF X_938 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center"])
    central_line(model, X_1, X_3, 1, 3)
    central_line(model, X_34, X_269, 34, 269)
    X_1467 = intersect_lines(model, X_1, X_3, X_34, X_269, ID="X_1467", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_452 = point_from_barycentrics(model, A, B, C, 0.36184857, 0.35103245, 0.28711898, ID="X_452", classes=["center", "incident"])
    central_line(model, X_7, X_452, 7, 452, incident=True)
    return promote_point_to_top(model, X_1467)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1467 on the given reference triangle."""
    model = create_model('X_1467 = X_938-BETH CONJUGATE OF X_938')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01467(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01467.json"))
    write_center_svg(
        model_acute,
        here / "x-01467.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
