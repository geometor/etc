"""GEOMETOR construction model for X(313) = ISOTOMIC CONJUGATE OF X(58)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00313(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(313) = ISOTOMIC CONJUGATE OF X(58) on reference triangle ABC."""
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center"])
    X_313 = isotomic_conjugate(model, A, B, C, X_58, ID="X(313)", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_10, X_75, 10, 75, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X(71)", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X(190)", classes=["center", "incident"])
    central_line(model, X_71, X_190, 71, 190, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    X_308 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b**(2) + c**(2))', ID="X(308)", classes=["center", "incident"])
    central_line(model, X_42, X_308, 42, 308, incident=True)
    return promote_point_to_top(model, X_313)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(313) on the given reference triangle."""
    model = create_model('X(313) = ISOTOMIC CONJUGATE OF X(58)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00313(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00313.json"))
    write_center_svg(
        model_acute,
        here / "x-00313.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
