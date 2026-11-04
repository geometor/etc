"""GEOMETOR construction model for X_1370 = ANTICOMPLEMENT OF X_25."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01370(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1370 = ANTICOMPLEMENT OF X_25 on reference triangle ABC."""
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_1368 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2)/(a**(2) - b**(2) + c**(2)) + c**(2)/(a**(2) + b**(2) - c**(2)))', ID="X_1368", classes=["center"])
    X_1370 = reflection_in_point(model, X_25, X_1368, ID="X_1370", classes=["selected", "target"], guide=False)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_66, X_69, 66, 69, incident=True)
    X_305 = eval_trilinear_point(model, A, B, C, 'b**(4)*c**(4)*cos(A)', ID="X_305", classes=["center", "incident"])
    X_315 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(4))', ID="X_315", classes=["center", "incident"])
    central_line(model, X_305, X_315, 305, 315, incident=True)
    return promote_point_to_top(model, X_1370)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1370 on the given reference triangle."""
    model = create_model('X_1370 = ANTICOMPLEMENT OF X_25')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01370(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01370.json"))
    write_center_svg(
        model_acute,
        here / "x-01370.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
