"""GEOMETOR construction model for X_2162 = X_2-ISOCONJUGATE OF X_43."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02162(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2162 = X_2-ISOCONJUGATE OF X_43 on reference triangle ABC."""
    X_192 = eval_trilinear_point(model, A, B, C, 'b*c*(c*a + a*b - b*c)', ID="X_192", classes=["center"])
    X_2162 = isogonal_conjugate(model, A, B, C, X_192, ID="X_2162", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    central_line(model, X_6, X_43, 6, 43, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_172 = eval_trilinear_point(model, A, B, C, 'a**(3) + a*b*c', ID="X_172", classes=["center", "incident"])
    central_line(model, X_31, X_172, 31, 172, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_330 = eval_trilinear_point(model, A, B, C, 'b*c/(a*b + a*c - b*c)', ID="X_330", classes=["center", "incident"])
    central_line(model, X_81, X_330, 81, 330, incident=True)
    return promote_point_to_top(model, X_2162)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2162 on the given reference triangle."""
    model = create_model('X_2162 = X_2-ISOCONJUGATE OF X_43')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02162(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02162.json"))
    write_center_svg(
        model_acute,
        here / "x-02162.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
