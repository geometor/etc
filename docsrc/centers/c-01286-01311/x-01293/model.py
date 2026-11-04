"""GEOMETOR construction model for X_1293 = COLLINGS TRANSFORM OF X_121."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01293(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1293 = COLLINGS TRANSFORM OF X_121 on reference triangle ABC."""
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X_649", classes=["center"])
    X_1293 = cevapoint(model, A, B, C, X_55, X_649, ID="X_1293", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    central_line(model, X_3, X_106, 3, 106, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_121 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - 2*a)*(b**(3) + c**(3) + a*(b**(2) + c**(2)) - 2*b*c*(b + c)))', ID="X_121", classes=["center", "incident"])
    central_line(model, X_4, X_121, 4, 121, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_40, X_104, 40, 104, incident=True)
    return promote_point_to_top(model, X_1293)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1293 on the given reference triangle."""
    model = create_model('X_1293 = COLLINGS TRANSFORM OF X_121')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01293(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01293.json"))
    write_center_svg(
        model_acute,
        here / "x-01293.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
