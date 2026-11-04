"""GEOMETOR construction model for X_2213 = X_2-ISOCONJUGATE OF X_380."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02213(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2213 = X_2-ISOCONJUGATE OF X_380 on reference triangle ABC."""
    X_452 = point_from_barycentrics(model, A, B, C, 0.36184857, 0.35103245, 0.28711898, ID="X_452", classes=["center"])
    X_2213 = isogonal_conjugate(model, A, B, C, X_452, ID="X_2213", classes=["selected", "target"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_56, X_71, 56, 71, incident=True)
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_57, X_72, 57, 72, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1412 = eval_trilinear_point(model, A, B, C, 'a/((b + c)*(a - b - c))', ID="X_1412", classes=["center", "incident"])
    central_line(model, X_3, X_1412, 3, 1412, incident=True)
    return promote_point_to_top(model, X_2213)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2213 on the given reference triangle."""
    model = create_model('X_2213 = X_2-ISOCONJUGATE OF X_380')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02213(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02213.json"))
    write_center_svg(
        model_acute,
        here / "x-02213.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
