"""GEOMETOR construction model for X_2204 = X_2-ISOCONJUGATE OF X_307."""

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


def construct_x_02204(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2204 = X_2-ISOCONJUGATE OF X_307 on reference triangle ABC."""
    X_1231 = point_from_barycentrics(model, A, B, C, 0.52872821, 0.34344739, 0.1278244, ID="X_1231", classes=["center"])
    X_2204 = isogonal_conjugate(model, A, B, C, X_1231, ID="X_2204", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_25, X_32, 25, 32, incident=True)
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_28, X_105, 28, 105, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_270 = eval_trilinear_point(model, A, B, C, '(sec(A))/(1 + cos(B - C))', ID="X_270", classes=["center", "incident"])
    central_line(model, X_21, X_270, 21, 270, incident=True)
    return promote_point_to_top(model, X_2204)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2204 on the given reference triangle."""
    model = create_model('X_2204 = X_2-ISOCONJUGATE OF X_307')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02204(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02204.json"))
    write_center_svg(
        model_acute,
        here / "x-02204.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
