"""GEOMETOR construction model for X_1936 = CROSSDIFFERENCE OF PU(15)."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01936(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1936 = CROSSDIFFERENCE OF PU(15) on reference triangle ABC."""
    X_1936 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2) - cos(B)*cos(C)', ID="X_1936", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_33, X_63, 33, 63, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_212 = eval_trilinear_point(model, A, B, C, '(cos(A))*(1 + cos(A))', ID="X_212", classes=["center", "incident"])
    central_line(model, X_2, X_212, 2, 212, incident=True)
    return promote_point_to_top(model, X_1936)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1936 on the given reference triangle."""
    model = create_model('X_1936 = CROSSDIFFERENCE OF PU(15)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01936(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01936.json"))
    write_center_svg(
        model_acute,
        here / "x-01936.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
