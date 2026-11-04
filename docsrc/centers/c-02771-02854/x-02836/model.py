"""GEOMETOR construction model for X_2836 = ISOGONAL CONJUGATE OF X_2752."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02836(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2836 = ISOGONAL CONJUGATE OF X_2752 on reference triangle ABC."""
    X_2752 = point_from_barycentrics(model, A, B, C, 0.80645161, -0.25806452, 0.4516129, ID="X_2752", classes=["center"])
    X_2836 = isogonal_conjugate(model, A, B, C, X_2752, ID="X_2836", classes=["selected", "target"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_67", classes=["center", "incident"])
    X_72 = eval_trilinear_point(model, A, B, C, '(b + c)*cot(A)', ID="X_72", classes=["center", "incident"])
    central_line(model, X_67, X_72, 67, 72, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_81, X_105, 81, 105, incident=True)
    X_120 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a*b*c - (b + c)*(a**(2) + (b - c)**(2)))*(b**(2) + c**(2) - a*b -a*c)', ID="X_120", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_120, X_125, 120, 125, incident=True)
    return promote_point_to_top(model, X_2836)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2836 on the given reference triangle."""
    model = create_model('X_2836 = ISOGONAL CONJUGATE OF X_2752')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02836(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02836.json"))
    write_center_svg(
        model_acute,
        here / "x-02836.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
