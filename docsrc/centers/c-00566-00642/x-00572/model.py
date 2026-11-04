"""GEOMETOR construction model for X_572 = ORTHOGONAL OF X_58."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00572(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_572 = ORTHOGONAL OF X_58 on reference triangle ABC."""
    X_572 = eval_trilinear_point(model, A, B, C, '(cos(A - U))', ID="X_572", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_9, X_48, 9, 48, incident=True)
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_54, X_71, 54, 71, incident=True)
    return promote_point_to_top(model, X_572)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_572 on the given reference triangle."""
    model = create_model('X_572 = ORTHOGONAL OF X_58')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00572(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00572.json"))
    write_center_svg(
        model_acute,
        here / "x-00572.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
