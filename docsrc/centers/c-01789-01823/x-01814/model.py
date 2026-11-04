"""GEOMETOR construction model for X_1814 = INVERSE MIMOSA TRANSFORM OF X_672."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    promote_point_to_top,
    reflection_in_point,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01814(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1814 = INVERSE MIMOSA TRANSFORM OF X_672 on reference triangle ABC."""
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X_651", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_1814 = reflection_in_point(model, X_651, X_6, ID="X_1814", classes=["selected", "target"], guide=False)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_6, X_7, 6, 7, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_48, X_77, 48, 77, incident=True)
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X_81", classes=["center", "incident"])
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center", "incident"])
    central_line(model, X_81, X_105, 81, 105, incident=True)
    return promote_point_to_top(model, X_1814)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1814 on the given reference triangle."""
    model = create_model('X_1814 = INVERSE MIMOSA TRANSFORM OF X_672')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01814(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01814.json"))
    write_center_svg(
        model_acute,
        here / "x-01814.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
