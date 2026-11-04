"""GEOMETOR construction model for X_2524 = RADICAL CENTER OF {NINE-POINT, BROCARD, 2nd BROCARD} CIRCLES."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02524(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2524 = RADICAL CENTER OF {NINE-POINT, BROCARD, 2nd BROCARD} CIRCLES on reference triangle ABC."""
    X_2489 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) - c**(2))/(b**(2) + c**(2) - a**(2)))', ID="X_2489", classes=["center"])
    X_2507 = eval_trilinear_point(model, A, B, C, '(a*((b**(4) - c**(4))*a**(6) - (b**(8) - c**(8))*a**(2) + 2*b**(4)*c**(4)*(b**(2) - c**(2))))', ID="X_2507", classes=["center"])
    X_2524 = reflection_in_point(model, X_2489, X_2507, ID="X_2524", classes=["selected", "target"], guide=False)
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_39, X_512, 39, 512, incident=True)
    X_441 = point_from_barycentrics(model, A, B, C, 0.74590002, 0.58940921, -0.33530923, ID="X_441", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_441, X_525, 441, 525, incident=True)
    central_line(model, X_2489, X_2507, 2489, 2507, incident=True)
    return promote_point_to_top(model, X_2524)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2524 on the given reference triangle."""
    model = create_model('X_2524 = RADICAL CENTER OF {NINE-POINT, BROCARD, 2nd BROCARD} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02524(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02524.json"))
    write_center_svg(
        model_acute,
        here / "x-02524.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
