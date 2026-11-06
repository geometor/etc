"""GEOMETOR construction model for X_3502 = ISOGONAL CONJUGATE OF X_3494."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03502(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3502 = ISOGONAL CONJUGATE OF X_3494 on reference triangle ABC."""
    X_3494 = eval_trilinear_point(model, A, B, C, '((a**(2) + b**(2) + c**(2) - a*b - a*c + b*c)/(a*b + a*c - b*c))', ID="X_3494", classes=["center"])
    X_3502 = isogonal_conjugate(model, A, B, C, X_3494, ID="X_3502", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2896 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(4) + b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2))', ID="X_2896", classes=["center", "incident"])
    central_line(model, X_1, X_2896, 1, 2896, incident=True)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_3496 = eval_trilinear_point(model, A, B, C, '(b**(3) + c**(3) - a**(3) + a*b*c)', ID="X_3496", classes=["center", "incident"])
    central_line(model, X_39, X_3496, 39, 3496, incident=True)
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X_384", classes=["center", "incident"])
    central_line(model, X_384, X_3494, 384, 3494, incident=True)
    return promote_point_to_top(model, X_3502)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3502 on the given reference triangle."""
    model = create_model('X_3502 = ISOGONAL CONJUGATE OF X_3494')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03502(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03502.json"))
    write_center_svg(
        model_acute,
        here / "x-03502.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
