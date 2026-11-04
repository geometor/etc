"""GEOMETOR construction model for X_2209 = X_2-ISOCONJUGATE OF X_330."""

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
    nagel_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02209(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2209 = X_2-ISOCONJUGATE OF X_330 on reference triangle ABC."""
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_2209 = ceva_conjugate(model, A, B, C, X_32, X_31, ID="X_2209", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_8, X_238, 8, 238, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    X_750 = eval_trilinear_point(model, A, B, C, 'a**(2) + 2*b*c', ID="X_750", classes=["center", "incident"])
    central_line(model, X_86, X_750, 86, 750, incident=True)
    return promote_point_to_top(model, X_2209)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2209 on the given reference triangle."""
    model = create_model('X_2209 = X_2-ISOCONJUGATE OF X_330')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02209(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02209.json"))
    write_center_svg(
        model_acute,
        here / "x-02209.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
