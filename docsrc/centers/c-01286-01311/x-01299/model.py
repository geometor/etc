"""GEOMETOR construction model for X_1299 = COLLINGS TRANSFORM OF X_135."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01299(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1299 = COLLINGS TRANSFORM OF X_135 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_135 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B))/(sec(2*C) - sec(2*A)) + (sin(2*C))/(sec(2*A) - sec(2*B)))', ID="X_135", classes=["center"])
    X_1299 = reflection_in_point(model, X_4, X_135, ID="X_1299", classes=["selected", "target"], guide=False)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_24, X_110, 24, 110, incident=True)
    X_131 = point_from_barycentrics(model, A, B, C, 0.57236082, 0.12379803, 0.30384114, ID="X_131", classes=["center", "incident"])
    central_line(model, X_4, X_131, 4, 131, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_317 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)*(csc(A))**(2)', ID="X_317", classes=["center", "incident"])
    central_line(model, X_99, X_317, 99, 317, incident=True)
    return promote_point_to_top(model, X_1299)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1299 on the given reference triangle."""
    model = create_model('X_1299 = COLLINGS TRANSFORM OF X_135')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01299(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01299.json"))
    write_center_svg(
        model_acute,
        here / "x-01299.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
