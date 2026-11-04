"""GEOMETOR construction model for X_1838 = ZOSMA TRANSFORM OF X_35."""

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
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01838(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1838 = ZOSMA TRANSFORM OF X_35 on reference triangle ABC."""
    X_1794 = point_from_barycentrics(model, A, B, C, 0.46882064, 0.38927507, 0.14190429, ID="X_1794", classes=["center"])
    X_1838 = isogonal_conjugate(model, A, B, C, X_1794, ID="X_1838", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    central_line(model, X_28, X_36, 28, 36, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_19, X_46, 19, 46, incident=True)
    return promote_point_to_top(model, X_1838)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1838 on the given reference triangle."""
    model = create_model('X_1838 = ZOSMA TRANSFORM OF X_35')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01838(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01838.json"))
    write_center_svg(
        model_acute,
        here / "x-01838.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
