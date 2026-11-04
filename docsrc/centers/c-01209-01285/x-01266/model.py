"""GEOMETOR construction model for X_1266 = ISOTOMIC CONJUGATE OF X_1120."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01266(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1266 = ISOTOMIC CONJUGATE OF X_1120 on reference triangle ABC."""
    X_1120 = eval_trilinear_point(model, A, B, C, '(b*c/(b**(2) + c**(2) + b*a + c*a - 4*b*c))', ID="X_1120", classes=["center"])
    X_1266 = isotomic_conjugate(model, A, B, C, X_1120, ID="X_1266", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_10, X_75, 10, 75, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_7, X_145, 7, 145, incident=True)
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X_192", classes=["center", "incident"])
    central_line(model, X_142, X_192, 142, 192, incident=True)
    return promote_point_to_top(model, X_1266)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1266 on the given reference triangle."""
    model = create_model('X_1266 = ISOTOMIC CONJUGATE OF X_1120')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01266(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01266.json"))
    write_center_svg(
        model_acute,
        here / "x-01266.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
