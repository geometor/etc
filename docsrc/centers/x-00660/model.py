"""GEOMETOR construction model for X(660) = TRILINEAR POLE OF LINE X(1)X(39)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00660(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(660) = TRILINEAR POLE OF LINE X(1)X(39) on reference triangle ABC."""
    X_659 = eval_trilinear_point(model, A, B, C, '(a**(2) - b*c)*(b - c)', ID="X(659)", classes=["center"])
    X_660 = isogonal_conjugate(model, A, B, C, X_659, ID="X(660)", classes=["selected", "target"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X(44)", classes=["center", "incident"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X(292)", classes=["center", "incident"])
    central_line(model, X_44, X_292, 44, 292, incident=True)
    X_88 = eval_trilinear_point(model, A, B, C, '1/(b + c - 2*a)', ID="X(88)", classes=["center", "incident"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X(291)", classes=["center", "incident"])
    central_line(model, X_88, X_291, 88, 291, incident=True)
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X(239)", classes=["center", "incident"])
    X_335 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(2) - b*c)', ID="X(335)", classes=["center", "incident"])
    central_line(model, X_239, X_335, 239, 335, incident=True)
    return promote_point_to_top(model, X_660)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(660) on the given reference triangle."""
    model = create_model('X(660) = TRILINEAR POLE OF LINE X(1)X(39)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00660(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00660.json"))
    write_center_svg(
        model_acute,
        here / "x-00660.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
