"""GEOMETOR construction model for X_1949 = TRILINEAR POLE OF PU(19)."""

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
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01949(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1949 = TRILINEAR POLE OF PU(19) on reference triangle ABC."""
    X_1948 = eval_trilinear_point(model, A, B, C, '(((cos(A))**(2) - cos(B)*cos(C))*csc(2*A))', ID="X_1948", classes=["center"])
    X_1949 = isogonal_conjugate(model, A, B, C, X_1948, ID="X_1949", classes=["selected", "target"])
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center", "incident"])
    X_296 = eval_trilinear_point(model, A, B, C, '(cos(A))/((cos(A))**(2) - cos(B)*cos(C))', ID="X_296", classes=["center", "incident"])
    central_line(model, X_219, X_296, 219, 296, incident=True)
    X_108 = eval_trilinear_point(model, A, B, C, 'a/(sec(B) - sec(C))', ID="X_108", classes=["center", "incident"])
    X_1172 = point_from_barycentrics(model, A, B, C, 0.14979394, 0.23060383, 0.61960222, ID="X_1172", classes=["center", "incident"])
    central_line(model, X_108, X_1172, 108, 1172, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_1945 = eval_trilinear_point(model, A, B, C, '(a/((cos(A))**(2) - cos(B)*cos(C)))', ID="X_1945", classes=["center", "incident"])
    central_line(model, X_6, X_1945, 6, 1945, incident=True)
    return promote_point_to_top(model, X_1949)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1949 on the given reference triangle."""
    model = create_model('X_1949 = TRILINEAR POLE OF PU(19)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01949(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01949.json"))
    write_center_svg(
        model_acute,
        here / "x-01949.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
