"""GEOMETOR construction model for X_2976 = RADICAL CENTER OF {CIRCUMCIRCLE, INCIRCLE, AC-INCIRCLE}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    anticomplement,
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02976(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2976 = RADICAL CENTER OF {CIRCUMCIRCLE, INCIRCLE, AC-INCIRCLE} on reference triangle ABC."""
    X_2505 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(2*a**(3) - 5*(b + c)*a**(2) - (b + c)**(3) + 8*a*(b**(2) + c**(2))))', ID="X_2505", classes=["center"])
    X_2976 = anticomplement(model, A, B, C, X_2505, ID="X_2976", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_100, X_190, 100, 190, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_676 = eval_trilinear_point(model, A, B, C, '(b*c*(b - c)*(b**(3) + c**(3) - 2*a**(3) + (b + c)*(a**(2) - b*c)))', ID="X_676", classes=["center", "incident"])
    central_line(model, X_513, X_676, 513, 676, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_2505, 2, 2505, incident=True)
    return promote_point_to_top(model, X_2976)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2976 on the given reference triangle."""
    model = create_model('X_2976 = RADICAL CENTER OF {CIRCUMCIRCLE, INCIRCLE, AC-INCIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02976(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02976.json"))
    write_center_svg(
        model_acute,
        here / "x-02976.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
