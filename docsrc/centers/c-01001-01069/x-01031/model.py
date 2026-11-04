"""GEOMETOR construction model for X_1031 = CYCLOCEVIAN CONJUGATE OF X_6."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01031(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1031 = CYCLOCEVIAN CONJUGATE OF X_6 on reference triangle ABC."""
    X_1031 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) + b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2))', ID="X_1031", classes=["selected", "target"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center", "incident"])
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X_384", classes=["center", "incident"])
    central_line(model, X_141, X_384, 141, 384, incident=True)
    return promote_point_to_top(model, X_1031)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1031 on the given reference triangle."""
    model = create_model('X_1031 = CYCLOCEVIAN CONJUGATE OF X_6')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01031(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01031.json"))
    write_center_svg(
        model_acute,
        here / "x-01031.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
