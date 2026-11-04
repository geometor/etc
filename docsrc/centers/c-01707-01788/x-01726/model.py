"""GEOMETOR construction model for X_1726 = MIMOSA TRANSFORM OF X_75."""

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
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01726(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1726 = MIMOSA TRANSFORM OF X_75 on reference triangle ABC."""
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X_264", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1726 = ceva_conjugate(model, A, B, C, X_264, X_1, ID="X_1726", classes=["selected", "target"])
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X_184", classes=["center", "incident"])
    central_line(model, X_1, X_184, 1, 184, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_63, X_321, 63, 321, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_440 = point_from_barycentrics(model, A, B, C, 0.44199278, 0.40077713, 0.15723009, ID="X_440", classes=["center", "incident"])
    central_line(model, X_9, X_440, 9, 440, incident=True)
    return promote_point_to_top(model, X_1726)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1726 on the given reference triangle."""
    model = create_model('X_1726 = MIMOSA TRANSFORM OF X_75')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01726(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01726.json"))
    write_center_svg(
        model_acute,
        here / "x-01726.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
