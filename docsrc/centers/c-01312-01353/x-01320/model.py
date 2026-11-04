"""GEOMETOR construction model for X_1320 = ISOGONAL CONJUGATE OF X_1319."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    incenter_of,
    midpoint,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01320(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1320 = ISOGONAL CONJUGATE OF X_1319 on reference triangle ABC."""
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center"])
    X_149 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a**(3) + (a**(2) - b*c)*(b + c) + a*(b*c - b**(2) - c**(2))))', ID="X_149", classes=["center"])
    X_1320 = midpoint(model, X_145, X_149, ID="X_1320", classes=["selected", "target"], guide=False)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    central_line(model, X_8, X_11, 8, 11, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X_88", classes=["center", "incident"])
    central_line(model, X_1, X_88, 1, 88, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_4, X_145, 4, 145, incident=True)
    return promote_point_to_top(model, X_1320)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1320 on the given reference triangle."""
    model = create_model('X_1320 = ISOGONAL CONJUGATE OF X_1319')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01320(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01320.json"))
    write_center_svg(
        model_acute,
        here / "x-01320.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
