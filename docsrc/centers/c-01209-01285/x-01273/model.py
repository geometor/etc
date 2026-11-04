"""GEOMETOR construction model for X_1273 = ISOTOMIC CONJUGATE OF X_1141."""

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
    isotomic_conjugate,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01273(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1273 = ISOTOMIC CONJUGATE OF X_1141 on reference triangle ABC."""
    X_1141 = eval_trilinear_point(model, A, B, C, 'b*c/(16*D**(2) + (a**(2)+c**(2)-b**(2))*(a**(2)+b**(2)-c**(2)))*(16*D**(2) - 3*(b**(2)+c**(2)-a**(2))**(2))', ID="X_1141", classes=["center"])
    X_1273 = isotomic_conjugate(model, A, B, C, X_1141, ID="X_1273", classes=["selected", "target"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_54, X_69, 54, 69, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_231 = eval_trilinear_point(model, A, B, C, '(cos(B))*(4*(sin(C))**(2) - 1)*(cos(A)*sin(B) - sin(A)*cos(B)) - (cos(C))*(4*(sin(B))**(2) - 1)*(cos(C)*sin(A) - sin(C)*cos(A))', ID="X_231", classes=["center", "incident"])
    central_line(model, X_2, X_231, 2, 231, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_311 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*cos(B - C)', ID="X_311", classes=["center", "incident"])
    central_line(model, X_5, X_311, 5, 311, incident=True)
    return promote_point_to_top(model, X_1273)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1273 on the given reference triangle."""
    model = create_model('X_1273 = ISOTOMIC CONJUGATE OF X_1141')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01273(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01273.json"))
    write_center_svg(
        model_acute,
        here / "x-01273.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
