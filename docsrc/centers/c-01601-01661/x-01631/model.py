"""GEOMETOR construction model for X_1631 = TCC-PERSPECTOR OF X_366."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01631(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1631 = TCC-PERSPECTOR OF X_366 on reference triangle ABC."""
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1631 = ceva_conjugate(model, A, B, C, X_75, X_6, ID="X_1631", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    central_line(model, X_3, X_142, 3, 142, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_199 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) - a**(4) + (b**(2) + c**(2) - a**(2))*(b*c + c*a + a*b)))', ID="X_199", classes=["center", "incident"])
    central_line(model, X_55, X_199, 55, 199, incident=True)
    X_560 = eval_trilinear_point(model, A, B, C, 'a**(4)', ID="X_560", classes=["center", "incident"])
    central_line(model, X_6, X_560, 6, 560, incident=True)
    return promote_point_to_top(model, X_1631)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1631 on the given reference triangle."""
    model = create_model('X_1631 = TCC-PERSPECTOR OF X_366')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01631(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01631.json"))
    write_center_svg(
        model_acute,
        here / "x-01631.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
