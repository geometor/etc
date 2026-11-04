"""GEOMETOR construction model for X_1617 = TCC-PERSPECTOR OF X_57."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01617(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1617 = TCC-PERSPECTOR OF X_57 on reference triangle ABC."""
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center"])
    X_934 = eval_trilinear_point(model, A, B, C, '1/((b - c)*(b + c - a)**(2))', ID="X_934", classes=["center"])
    X_1617 = crosspoint(model, A, B, C, X_59, X_934, ID="X_1617", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_25, X_105, 25, 105, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_222 = eval_trilinear_point(model, A, B, C, 'cos(A)*tan(A/2)', ID="X_222", classes=["center", "incident"])
    central_line(model, X_31, X_222, 31, 222, incident=True)
    return promote_point_to_top(model, X_1617)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1617 on the given reference triangle."""
    model = create_model('X_1617 = TCC-PERSPECTOR OF X_57')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01617(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01617.json"))
    write_center_svg(
        model_acute,
        here / "x-01617.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
