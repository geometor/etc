"""GEOMETOR construction model for X_2796 = ISOGONAL CONJUGATE OF X_2712."""

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
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02796(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2796 = ISOGONAL CONJUGATE OF X_2712 on reference triangle ABC."""
    X_2712 = point_from_barycentrics(model, A, B, C, 0.50038452, -0.33025309, 0.82986858, ID="X_2712", classes=["center"])
    X_2796 = isogonal_conjugate(model, A, B, C, X_2712, ID="X_2796", classes=["selected", "target"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    central_line(model, X_86, X_99, 86, 99, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_10, X_190, 10, 190, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_121 = eval_trilinear_point(model, A, B, C, '(b*c*(b + c - 2*a)*(b**(3) + c**(3) + a*(b**(2) + c**(2)) - 2*b*c*(b + c)))', ID="X_121", classes=["center", "incident"])
    central_line(model, X_115, X_121, 115, 121, incident=True)
    return promote_point_to_top(model, X_2796)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2796 on the given reference triangle."""
    model = create_model('X_2796 = ISOGONAL CONJUGATE OF X_2712')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02796(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02796.json"))
    write_center_svg(
        model_acute,
        here / "x-02796.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
