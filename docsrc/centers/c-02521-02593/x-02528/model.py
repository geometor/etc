"""GEOMETOR construction model for X_2528 = RADICAL CENTER OF {ORTHOCENTROIDAL, BROCARD, (X_4,2R)} CIRCLES."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02528(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2528 = RADICAL CENTER OF {ORTHOCENTROIDAL, BROCARD, (X_4,2R)} CIRCLES on reference triangle ABC."""
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X_141", classes=["center"])
    X_2528 = ceva_conjugate(model, A, B, C, X_99, X_141, ID="X_2528", classes=["selected", "target"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    X_647 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))*(b**(2) + c**(2) - a**(2))', ID="X_647", classes=["center", "incident"])
    central_line(model, X_39, X_647, 39, 647, incident=True)
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X_669", classes=["center", "incident"])
    central_line(model, X_525, X_669, 525, 669, incident=True)
    X_826 = eval_trilinear_point(model, A, B, C, 'a **(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0))', ID="X_826", classes=["center", "incident"])
    X_2474 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) - c**(4))*(a**(4) + b**(4) + c**(4) + 2*a**(2)*b**(2) + 2*a**(2)*c**(2) - 2*b**(2)*c**(2)))', ID="X_2474", classes=["center", "incident"])
    central_line(model, X_826, X_2474, 826, 2474, incident=True)
    return promote_point_to_top(model, X_2528)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2528 on the given reference triangle."""
    model = create_model('X_2528 = RADICAL CENTER OF {ORTHOCENTROIDAL, BROCARD, (X_4,2R)} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02528(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02528.json"))
    write_center_svg(
        model_acute,
        here / "x-02528.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
