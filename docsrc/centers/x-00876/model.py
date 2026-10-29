"""GEOMETOR construction model for X(876) = ISOTOMIC CONJUGATE OF X(874)."""

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
    reflection_in_point,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00876(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(876) = ISOTOMIC CONJUGATE OF X(874) on reference triangle ABC."""
    X_659 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*(b - c)', ID="X(659)", classes=["center"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X(665)", classes=["center"])
    X_876 = reflection_in_point(model, X_659, X_665, ID="X(876)", classes=["selected", "target"], guide=False)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X(512)", classes=["center", "incident"])
    central_line(model, X_1, X_512, 1, 512, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X(514)", classes=["center", "incident"])
    central_line(model, X_10, X_514, 10, 514, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X(513)", classes=["center", "incident"])
    central_line(model, X_37, X_513, 37, 513, incident=True)
    return promote_point_to_top(model, X_876)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(876) on the given reference triangle."""
    model = create_model('X(876) = ISOTOMIC CONJUGATE OF X(874)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00876(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00876.json"))
    write_center_svg(
        model_acute,
        here / "x-00876.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
