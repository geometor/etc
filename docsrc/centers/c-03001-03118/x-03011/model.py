"""GEOMETOR construction model for X_3011 = (NAGEL LINE)∩(ORTHIC AXIS)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03011(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3011 = (NAGEL LINE)∩(ORTHIC AXIS) on reference triangle ABC."""
    X_3006 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(3) + c**(3) - a*b**(2) - a*c**(2)))', ID="X_3006", classes=["center"])
    X_3011 = complement(model, A, B, C, X_3006, ID="X_3011", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    central_line(model, X_25, X_225, 25, 225, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_226 = eval_trilinear_point(model, A, B, C, '(csc(A))*(cos(B) + cos(C))', ID="X_226", classes=["center", "incident"])
    central_line(model, X_31, X_226, 31, 226, incident=True)
    return promote_point_to_top(model, X_3011)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3011 on the given reference triangle."""
    model = create_model('X_3011 = (NAGEL LINE)∩(ORTHIC AXIS)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03011(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03011.json"))
    write_center_svg(
        model_acute,
        here / "x-03011.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
