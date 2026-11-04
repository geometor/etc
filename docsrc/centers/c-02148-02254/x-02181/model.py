"""GEOMETOR construction model for X_2181 = X_2-ISOCONJUGATE OF X_97."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02181(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2181 = X_2-ISOCONJUGATE OF X_97 on reference triangle ABC."""
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center"])
    X_2179 = point_from_barycentrics(model, A, B, C, 0.14560228, 0.26857992, 0.5858178, ID="X_2179", classes=["center"])
    X_2181 = ceva_conjugate(model, A, B, C, X_19, X_2179, ID="X_2181", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_19, X_31, 19, 31, incident=True)
    X_38 = eval_trilinear_point(model, A, B, C, 'b**(2) + c**(2)', ID="X_38", classes=["center", "incident"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    central_line(model, X_38, X_92, 38, 92, incident=True)
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    X_278 = eval_trilinear_point(model, A, B, C, 'sec(A)*tan(A/2)', ID="X_278", classes=["center", "incident"])
    central_line(model, X_244, X_278, 244, 278, incident=True)
    return promote_point_to_top(model, X_2181)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2181 on the given reference triangle."""
    model = create_model('X_2181 = X_2-ISOCONJUGATE OF X_97')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02181(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02181.json"))
    write_center_svg(
        model_acute,
        here / "x-02181.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
