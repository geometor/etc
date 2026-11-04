"""GEOMETOR construction model for X_2743 = SR(X_104, X_106)."""

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
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02743(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2743 = SR(X_104, X_106) on reference triangle ABC."""
    X_2718 = eval_trilinear_point(model, A, B, C, '(1/(b**(3) + c**(3) - a**(2)*b - a**(2)*c - 2*b**(2)*c - 2*b*c**(2) + 4*a*b*c))', ID="X_2718", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2743 = reflection_in_point(model, X_2718, X_3, ID="X_2743", classes=["selected", "target"], guide=False)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center", "incident"])
    central_line(model, X_104, X_519, 104, 519, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X_517", classes=["center", "incident"])
    central_line(model, X_106, X_517, 106, 517, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_953 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(4) - 2*a**(3)*(b + c) - a**(2)*(b**(2) - 4*b*c + c**(2)) + (2*a - b - c)*(b - c)*(b**(2) - c**(2)))', ID="X_953", classes=["center", "incident"])
    central_line(model, X_40, X_953, 40, 953, incident=True)
    return promote_point_to_top(model, X_2743)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2743 on the given reference triangle."""
    model = create_model('X_2743 = SR(X_104, X_106)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02743(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02743.json"))
    write_center_svg(
        model_acute,
        here / "x-02743.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
