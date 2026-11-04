"""GEOMETOR construction model for X_1509 = ISOGONAL CONJUGATE OF X_1500."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01509(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1509 = ISOGONAL CONJUGATE OF X_1500 on reference triangle ABC."""
    X_1500 = eval_trilinear_point(model, A, B, C, 'a*(b + c)**(2)', ID="X_1500", classes=["center"])
    X_1509 = isogonal_conjugate(model, A, B, C, X_1500, ID="X_1509", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_1, X_99, 1, 99, incident=True)
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X_58", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_58, X_86, 58, 86, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    central_line(model, X_81, X_239, 81, 239, incident=True)
    return promote_point_to_top(model, X_1509)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1509 on the given reference triangle."""
    model = create_model('X_1509 = ISOGONAL CONJUGATE OF X_1500')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01509(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01509.json"))
    write_center_svg(
        model_acute,
        here / "x-01509.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
