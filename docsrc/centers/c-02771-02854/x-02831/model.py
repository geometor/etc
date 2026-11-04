"""GEOMETOR construction model for X_2831 = ISOGONAL CONJUGATE OF X_2747."""

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


def construct_x_02831(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2831 = ISOGONAL CONJUGATE OF X_2747 on reference triangle ABC."""
    X_2747 = point_from_barycentrics(model, A, B, C, 1.0413593, 0.2727953, -0.31415458, ID="X_2747", classes=["center"])
    X_2831 = isogonal_conjugate(model, A, B, C, X_2747, ID="X_2831", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X_132", classes=["center", "incident"])
    central_line(model, X_11, X_132, 11, 132, incident=True)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_104, X_112, 104, 112, incident=True)
    X_119 = eval_trilinear_point(model, A, B, C, '(csc(A))*(-1 + cos(B) + cos(C))*(sin(2*B) + sin(2*C) + 2*(-1 + cos(A))*(sin(B) + sin(C)))', ID="X_119", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X_127", classes=["center", "incident"])
    central_line(model, X_119, X_127, 119, 127, incident=True)
    return promote_point_to_top(model, X_2831)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2831 on the given reference triangle."""
    model = create_model('X_2831 = ISOGONAL CONJUGATE OF X_2747')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02831(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02831.json"))
    write_center_svg(
        model_acute,
        here / "x-02831.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
