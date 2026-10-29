"""GEOMETOR construction model for X(875) = ISOGONAL CONJUGATE OF X(874)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_00875(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(875) = ISOGONAL CONJUGATE OF X(874) on reference triangle ABC."""
    X_874 = point_from_barycentrics(model, A, B, C, 4.4210526, 0.10835913, -3.5294118, ID="X(874)", classes=["center"])
    X_875 = isogonal_conjugate(model, A, B, C, X_874, ID="X(875)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X(512)", classes=["center", "incident"])
    central_line(model, X_1, X_512, 1, 512, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X(42)", classes=["center", "incident"])
    X_649 = eval_trilinear_point(model, A, B, C, 'a*(b - c)', ID="X(649)", classes=["center", "incident"])
    central_line(model, X_42, X_649, 42, 649, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_669 = eval_trilinear_point(model, A, B, C, 'a**(3)*(b**(2) - c**(2))', ID="X(669)", classes=["center", "incident"])
    central_line(model, X_31, X_669, 31, 669, incident=True)
    return promote_point_to_top(model, X_875)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(875) on the given reference triangle."""
    model = create_model('X(875) = ISOGONAL CONJUGATE OF X(874)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00875(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00875.json"))
    write_center_svg(
        model_acute,
        here / "x-00875.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
