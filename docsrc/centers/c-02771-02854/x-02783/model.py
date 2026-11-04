"""GEOMETOR construction model for X_2783 = ISOGONAL CONJUGATE OF X_2699."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02783(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2783 = ISOGONAL CONJUGATE OF X_2699 on reference triangle ABC."""
    X_2699 = point_from_barycentrics(model, A, B, C, 0.82718162, -0.2432613, 0.41607968, ID="X_2699", classes=["center"])
    X_2783 = isogonal_conjugate(model, A, B, C, X_2699, ID="X_2783", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    central_line(model, X_11, X_114, 11, 114, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    central_line(model, X_98, X_100, 98, 100, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    central_line(model, X_99, X_104, 99, 104, incident=True)
    return promote_point_to_top(model, X_2783)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2783 on the given reference triangle."""
    model = create_model('X_2783 = ISOGONAL CONJUGATE OF X_2699')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02783(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02783.json"))
    write_center_svg(
        model_acute,
        here / "x-02783.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
