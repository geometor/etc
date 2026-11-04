"""GEOMETOR construction model for X_2329 = X_2-ISOCONJUGATE OF X_1431."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02329(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2329 = X_2-ISOCONJUGATE OF X_1431 on reference triangle ABC."""
    X_1432 = point_from_barycentrics(model, A, B, C, 0.20472746, 0.30910962, 0.48616292, ID="X_1432", classes=["center"])
    X_2329 = isogonal_conjugate(model, A, B, C, X_1432, ID="X_2329", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    central_line(model, X_8, X_41, 8, 41, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_10, X_98, 10, 98, incident=True)
    return promote_point_to_top(model, X_2329)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2329 on the given reference triangle."""
    model = create_model('X_2329 = X_2-ISOCONJUGATE OF X_1431')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02329(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02329.json"))
    write_center_svg(
        model_acute,
        here / "x-02329.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
