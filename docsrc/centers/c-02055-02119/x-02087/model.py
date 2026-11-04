"""GEOMETOR construction model for X_2087 = PK-TRANSFORM OF X_100."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02087(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2087 = PK-TRANSFORM OF X_100 on reference triangle ABC."""
    X_2087 = eval_trilinear_point(model, A, B, C, '(b + c - 2*a)*(b - c)**(2)', ID="X_2087", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X_665", classes=["center", "incident"])
    central_line(model, X_244, X_665, 244, 665, incident=True)
    X_1914 = eval_trilinear_point(model, A, B, C, '1 - a**(2)/(b*c)', ID="X_1914", classes=["center", "incident"])
    X_1983 = eval_trilinear_point(model, A, B, C, '(sin(C - A) - sin(A - B))/sin(B - C)', ID="X_1983", classes=["center", "incident"])
    central_line(model, X_1914, X_1983, 1914, 1983, incident=True)
    return promote_point_to_top(model, X_2087)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2087 on the given reference triangle."""
    model = create_model('X_2087 = PK-TRANSFORM OF X_100')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02087(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02087.json"))
    write_center_svg(
        model_acute,
        here / "x-02087.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
