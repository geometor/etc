"""GEOMETOR construction model for X_2326 = X_2-ISOCONJUGATE OF X_1425."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02326(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2326 = X_2-ISOCONJUGATE OF X_1425 on reference triangle ABC."""
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center"])
    X_1172 = point_from_barycentrics(model, A, B, C, 0.14979394, 0.23060383, 0.61960222, ID="X_1172", classes=["center"])
    X_2326 = cevapoint(model, A, B, C, X_284, X_1172, ID="X_2326", classes=["selected", "target"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_27, X_86, 27, 86, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_162 = eval_trilinear_point(model, A, B, C, '1/(sin(2*B) - sin(2*C))', ID="X_162", classes=["center", "incident"])
    central_line(model, X_6, X_162, 6, 162, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    X_270 = eval_trilinear_point(model, A, B, C, '(sec(A))/(1 + cos(B - C))', ID="X_270", classes=["center", "incident"])
    central_line(model, X_21, X_270, 21, 270, incident=True)
    return promote_point_to_top(model, X_2326)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2326 on the given reference triangle."""
    model = create_model('X_2326 = X_2-ISOCONJUGATE OF X_1425')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02326(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02326.json"))
    write_center_svg(
        model_acute,
        here / "x-02326.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
