"""GEOMETOR construction model for X(452) = X(2)-HIRST INVERSE OF X(449)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00452(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(452) = X(2)-HIRST INVERSE OF X(449) on reference triangle ABC."""
    X_443 = point_from_barycentrics(model, A, B, C, 0.31907571, 0.32448378, 0.35644051, ID="X(443)", classes=["center"])
    X_452 = anticomplement(model, A, B, C, X_443, ID="X(452)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_8, X_9, 8, 9, incident=True)
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X(72)", classes=["center", "incident"])
    X_145 = eval_trilinear_point(model, A, B, C, 'b*c*(3*a - b - c)', ID="X(145)", classes=["center", "incident"])
    central_line(model, X_72, X_145, 72, 145, incident=True)
    return promote_point_to_top(model, X_452)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(452) on the given reference triangle."""
    model = create_model('X(452) = X(2)-HIRST INVERSE OF X(449)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00452(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00452.json"))
    write_center_svg(
        model_acute,
        here / "x-00452.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
