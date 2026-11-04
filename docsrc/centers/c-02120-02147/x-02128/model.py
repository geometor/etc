"""GEOMETOR construction model for X_2128 = EIGENTRANSFORM OF X_19."""

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
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02128(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2128 = EIGENTRANSFORM OF X_19 on reference triangle ABC."""
    X_2128 = eval_trilinear_point(model, A, B, C, '((b**(2) + c**(2) - a**(2))*((a**(2) + b**(2) + c**(2))**(2) - 8*b**(2)*c**(2)))', ID="X_2128", classes=["selected", "target"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_304 = eval_trilinear_point(model, A, B, C, '(cot(A))*(csc(A))**(2)', ID="X_304", classes=["center", "incident"])
    central_line(model, X_63, X_304, 63, 304, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_1958 = eval_trilinear_point(model, A, B, C, '((cot(A))**(2) + cot(B)*cot(C))', ID="X_1958", classes=["center", "incident"])
    central_line(model, X_1, X_1958, 1, 1958, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_2082 = eval_trilinear_point(model, A, B, C, '(b + c - a)*(a**(2) + (b - c)**(2))', ID="X_2082", classes=["center", "incident"])
    central_line(model, X_2, X_2082, 2, 2082, incident=True)
    return promote_point_to_top(model, X_2128)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2128 on the given reference triangle."""
    model = create_model('X_2128 = EIGENTRANSFORM OF X_19')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02128(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02128.json"))
    write_center_svg(
        model_acute,
        here / "x-02128.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
