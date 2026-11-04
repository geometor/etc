"""GEOMETOR construction model for X_2220 = X_2-ISOCONJUGATE OF X_596."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02220(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2220 = X_2-ISOCONJUGATE OF X_596 on reference triangle ABC."""
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center"])
    X_1252 = point_from_barycentrics(model, A, B, C, 0.30120482, 0.10843373, 0.59036145, ID="X_1252", classes=["center"])
    X_2220 = crosspoint(model, A, B, C, X_163, X_1252, ID="X_2220", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    central_line(model, X_37, X_82, 37, 82, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_872 = eval_trilinear_point(model, A, B, C, '(a*(b + c))**(2)', ID="X_872", classes=["center", "incident"])
    central_line(model, X_31, X_872, 31, 872, incident=True)
    return promote_point_to_top(model, X_2220)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2220 on the given reference triangle."""
    model = create_model('X_2220 = X_2-ISOCONJUGATE OF X_596')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02220(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02220.json"))
    write_center_svg(
        model_acute,
        here / "x-02220.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
