"""GEOMETOR construction model for X_2476 = INVERSE-IN-ORTHOCENTROIDAL-CIRCLE OF X_21."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02476(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2476 = INVERSE-IN-ORTHOCENTROIDAL-CIRCLE OF X_21 on reference triangle ABC."""
    X_2476 = eval_trilinear_point(model, A, B, C, '(b*c*(a*b*c*(b + c) - (b**(2) - c**(2))**(2) + a**(2)*(b**(2) + b*c + c**(2))))', ID="X_2476", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    central_line(model, X_8, X_12, 8, 12, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_498 = eval_trilinear_point(model, A, B, C, '1 + 2*sin(B)*sin(C)', ID="X_498", classes=["center", "incident"])
    central_line(model, X_100, X_498, 100, 498, incident=True)
    return promote_point_to_top(model, X_2476)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2476 on the given reference triangle."""
    model = create_model('X_2476 = INVERSE-IN-ORTHOCENTROIDAL-CIRCLE OF X_21')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02476(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02476.json"))
    write_center_svg(
        model_acute,
        here / "x-02476.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
