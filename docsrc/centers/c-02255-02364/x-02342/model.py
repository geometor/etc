"""GEOMETOR construction model for X_2342 = X_2-ISOCONJUGATE OF X_1465."""

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
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02342(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2342 = X_2-ISOCONJUGATE OF X_1465 on reference triangle ABC."""
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center"])
    X_909 = point_from_barycentrics(model, A, B, C, 0.29761905, 1.2857143, -0.58333333, ID="X_909", classes=["center"])
    X_2342 = ceva_conjugate(model, A, B, C, X_104, X_909, ID="X_2342", classes=["selected", "target"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    central_line(model, X_31, X_33, 31, 33, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    central_line(model, X_1, X_104, 1, 104, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_55, X_184, 55, 184, incident=True)
    return promote_point_to_top(model, X_2342)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2342 on the given reference triangle."""
    model = create_model('X_2342 = X_2-ISOCONJUGATE OF X_1465')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02342(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02342.json"))
    write_center_svg(
        model_acute,
        here / "x-02342.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
