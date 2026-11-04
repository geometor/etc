"""GEOMETOR construction model for X_1240 = ISOTOMIC CONJUGATE OF X_1193."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01240(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1240 = ISOTOMIC CONJUGATE OF X_1193 on reference triangle ABC."""
    X_1193 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + c**(2) + a*b + a*c))', ID="X_1193", classes=["center"])
    X_1240 = isotomic_conjugate(model, A, B, C, X_1193, ID="X_1240", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_7, X_76, 7, 76, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    X_313 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(3)*c**(3)', ID="X_313", classes=["center", "incident"])
    central_line(model, X_86, X_313, 86, 313, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_1237 = eval_trilinear_point(model, A, B, C, '(b**(3)*c**(3)*(b + c)*(a**(2) + b*c))', ID="X_1237", classes=["center", "incident"])
    central_line(model, X_75, X_1237, 75, 1237, incident=True)
    return promote_point_to_top(model, X_1240)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1240 on the given reference triangle."""
    model = create_model('X_1240 = ISOTOMIC CONJUGATE OF X_1193')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01240(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01240.json"))
    write_center_svg(
        model_acute,
        here / "x-01240.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
