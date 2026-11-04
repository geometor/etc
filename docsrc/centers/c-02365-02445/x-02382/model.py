"""GEOMETOR construction model for X_2382 = CIR(X_537)."""

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


def construct_x_02382(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2382 = CIR(X_537) on reference triangle ABC."""
    X_537 = point_from_barycentrics(model, A, B, C, 0.47409982, -0.81274255, 0.33864273, ID="X_537", classes=["center"])
    X_2382 = isogonal_conjugate(model, A, B, C, X_537, ID="X_2382", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_100, X_238, 100, 238, incident=True)
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center", "incident"])
    X_667 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b - c)', ID="X_667", classes=["center", "incident"])
    central_line(model, X_106, X_667, 106, 667, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_813 = eval_trilinear_point(model, A, B, C, '1/(a**(-2)*(b**(1) - c**(1)) + a**(0)*(b**(-1) - c **(-1)))', ID="X_813", classes=["center", "incident"])
    central_line(model, X_6, X_813, 6, 813, incident=True)
    return promote_point_to_top(model, X_2382)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2382 on the given reference triangle."""
    model = create_model('X_2382 = CIR(X_537)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02382(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02382.json"))
    write_center_svg(
        model_acute,
        here / "x-02382.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
