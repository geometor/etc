"""GEOMETOR construction model for X_2794 = ISOGONAL CONJUGATE OF X_2710."""

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
    isogonal_conjugate,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02794(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2794 = ISOGONAL CONJUGATE OF X_2710 on reference triangle ABC."""
    X_2710 = point_from_barycentrics(model, A, B, C, 1.0405687, 0.20733336, -0.24790201, ID="X_2710", classes=["center"])
    X_2794 = isogonal_conjugate(model, A, B, C, X_2710, ID="X_2794", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_4, X_32, 4, 32, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    central_line(model, X_3, X_114, 3, 114, incident=True)
    X_20 = eval_trilinear_point(model, A, B, C, 'cos(A) - cos(B)*cos(C)', ID="X_20", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_20, X_99, 20, 99, incident=True)
    return promote_point_to_top(model, X_2794)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2794 on the given reference triangle."""
    model = create_model('X_2794 = ISOGONAL CONJUGATE OF X_2710')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02794(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02794.json"))
    write_center_svg(
        model_acute,
        here / "x-02794.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
