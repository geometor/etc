"""GEOMETOR construction model for X(870) = ISOGONAL CONJUGATE OF X(869)."""

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
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00870(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(870) = ISOGONAL CONJUGATE OF X(869) on reference triangle ABC."""
    X_869 = point_from_barycentrics(model, A, B, C, 0.22475648, 0.33333333, 0.44191018, ID="X(869)", classes=["center"])
    X_870 = isogonal_conjugate(model, A, B, C, X_869, ID="X(870)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_1, X_76, 1, 76, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_6, X_75, 6, 75, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    X_85 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(b + c - a)', ID="X(85)", classes=["center", "incident"])
    central_line(model, X_56, X_85, 56, 85, incident=True)
    return promote_point_to_top(model, X_870)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(870) on the given reference triangle."""
    model = create_model('X(870) = ISOGONAL CONJUGATE OF X(869)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00870(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00870.json"))
    write_center_svg(
        model_acute,
        here / "x-00870.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
