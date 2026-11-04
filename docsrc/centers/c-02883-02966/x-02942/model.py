"""GEOMETOR construction model for X_2942 = EXCENTRAL-ISOGONAL CONJUGATE OF X_7."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02942(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2942 = EXCENTRAL-ISOGONAL CONJUGATE OF X_7 on reference triangle ABC."""
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center"])
    X_169 = eval_trilinear_point(model, A, B, C, '- (sin(A))*(cos(A/2))**(2) + (sin(B))*(cos(B/2))**(2) + (sin(C))*(cos(C/2))**(2)', ID="X_169", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_1742 = eval_trilinear_point(model, A, B, C, '(sec(B/2))**(2) + (sec(C/2))**(2) - (sec(A/2))**(2)', ID="X_1742", classes=["center"])
    central_line(model, X_165, X_169, 165, 169)
    central_line(model, X_57, X_1742, 57, 1742)
    X_2942 = intersect_lines(model, X_165, X_169, X_57, X_1742, ID="X_2942", classes=["selected", "target"])
    X_1762 = point_from_barycentrics(model, A, B, C, 0.33791285, 0.30169303, 0.36039412, ID="X_1762", classes=["center", "incident"])
    X_2938 = point_from_barycentrics(model, A, B, C, 0.53750967, 0.44083527, 0.021655066, ID="X_2938", classes=["center", "incident"])
    central_line(model, X_1762, X_2938, 1762, 2938, incident=True)
    return promote_point_to_top(model, X_2942)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2942 on the given reference triangle."""
    model = create_model('X_2942 = EXCENTRAL-ISOGONAL CONJUGATE OF X_7')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02942(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02942.json"))
    write_center_svg(
        model_acute,
        here / "x-02942.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
