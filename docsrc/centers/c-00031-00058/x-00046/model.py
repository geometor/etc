"""GEOMETOR construction model for X_46 = X_4-CEVA CONJUGATE OF X_1."""

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
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00046(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_46 = X_4-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_10, X_63, 10, 63, incident=True)
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    central_line(model, X_34, X_47, 34, 47, incident=True)
    return promote_point_to_top(model, X_46)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_46 on the given reference triangle."""
    model = create_model('X_46 = X_4-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00046(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00046.json"))
    write_center_svg(
        model_acute,
        here / "x-00046.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
