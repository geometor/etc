"""GEOMETOR construction model for X_3177 = X_9-CEVA CONJUGATE OF X_2."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_03177(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3177 = X_9-CEVA CONJUGATE OF X_2 on reference triangle ABC."""
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X_85", classes=["center"])
    X_1212 = eval_trilinear_point(model, A, B, C, '(a - b - c)*(b**(2) + c**(2) - a*b - a*c - 2*b*c)', ID="X_1212", classes=["center"])
    X_3177 = reflection_in_point(model, X_85, X_1212, ID="X_3177", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_85, 2, 85, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    central_line(model, X_63, X_194, 63, 194, incident=True)
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X_144", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X_145", classes=["center", "incident"])
    central_line(model, X_144, X_145, 144, 145, incident=True)
    return promote_point_to_top(model, X_3177)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3177 on the given reference triangle."""
    model = create_model('X_3177 = X_9-CEVA CONJUGATE OF X_2')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03177(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03177.json"))
    write_center_svg(
        model_acute,
        here / "x-03177.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
