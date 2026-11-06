"""GEOMETOR construction model for X_3768 = X_3250com[T(bc, b²)]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03768(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3768 = X_3250com[T(bc, b²)] on reference triangle ABC."""
    X_3768 = eval_barycentric_point(model, A, B, C, 'a**(2)*(b - c)*(2*b*c - a*b - a*c)', ID="X_3768", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_44, X_513, 44, 513, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_646 = eval_trilinear_point(model, A, B, C, '((b + c - a)/(a**(2)*(b - c)))', ID="X_646", classes=["center", "incident"])
    central_line(model, X_190, X_646, 190, 646, incident=True)
    X_1015 = eval_trilinear_point(model, A, B, C, 'a*(b - c)**(2)', ID="X_1015", classes=["center", "incident"])
    X_1960 = eval_trilinear_point(model, A, B, C, 'a*(b - c)*(2*a - b - c)', ID="X_1960", classes=["center", "incident"])
    central_line(model, X_1015, X_1960, 1015, 1960, incident=True)
    return promote_point_to_top(model, X_3768)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3768 on the given reference triangle."""
    model = create_model('X_3768 = X_3250com[T(bc, b²)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03768(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03768.json"))
    write_center_svg(
        model_acute,
        here / "x-03768.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
