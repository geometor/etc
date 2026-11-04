"""GEOMETOR construction model for X_341 = ISOTOMIC CONJUGATE OF X_269."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00341(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_341 = ISOTOMIC CONJUGATE OF X_269 on reference triangle ABC."""
    X_341 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*(b + c - a)**(2)', ID="X_341", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_10, X_75, 10, 75, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_210 = eval_trilinear_point(model, A, B, C, '(b + c)*(b + c - a)', ID="X_210", classes=["center", "incident"])
    central_line(model, X_8, X_210, 8, 210, incident=True)
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_40, X_190, 40, 190, incident=True)
    return promote_point_to_top(model, X_341)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_341 on the given reference triangle."""
    model = create_model('X_341 = ISOTOMIC CONJUGATE OF X_269')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00341(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00341.json"))
    write_center_svg(
        model_acute,
        here / "x-00341.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
