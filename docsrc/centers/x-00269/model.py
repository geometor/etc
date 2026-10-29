"""GEOMETOR construction model for X(269) = ISOGONAL CONJUGATE OF X(200)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00269(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(269) = ISOGONAL CONJUGATE OF X(200) on reference triangle ABC."""
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X(200)", classes=["center"])
    X_269 = isogonal_conjugate(model, A, B, C, X_200, ID="X(269)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X(57)", classes=["center", "incident"])
    central_line(model, X_6, X_57, 6, 57, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_241 = eval_trilinear_point(model, A, B, C, '(b**(2) + c**(2) - a*b - a*c)/(a - b - c)', ID="X(241)", classes=["center", "incident"])
    central_line(model, X_9, X_241, 9, 241, incident=True)
    return promote_point_to_top(model, X_269)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(269) on the given reference triangle."""
    model = create_model('X(269) = ISOGONAL CONJUGATE OF X(200)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00269(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00269.json"))
    write_center_svg(
        model_acute,
        here / "x-00269.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
