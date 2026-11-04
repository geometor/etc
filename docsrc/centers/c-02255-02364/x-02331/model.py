"""GEOMETOR construction model for X_2331 = X_2-ISOCONJUGATE OF X_1433."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02331(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2331 = X_2-ISOCONJUGATE OF X_1433 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center"])
    X_2331 = crosspoint(model, A, B, C, X_1, X_223, ID="X_2331", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    central_line(model, X_33, X_42, 33, 42, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_204 = eval_trilinear_point(model, A, B, C, '((tan(A))*(tan(B) + tan(C) - tan(A)))', ID="X_204", classes=["center", "incident"])
    central_line(model, X_55, X_204, 55, 204, incident=True)
    return promote_point_to_top(model, X_2331)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2331 on the given reference triangle."""
    model = create_model('X_2331 = X_2-ISOCONJUGATE OF X_1433')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02331(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02331.json"))
    write_center_svg(
        model_acute,
        here / "x-02331.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
