"""GEOMETOR construction model for X(268) = ISOGONAL CONJUGATE OF X(196)."""

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
    isogonal_conjugate,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00268(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(268) = ISOGONAL CONJUGATE OF X(196) on reference triangle ABC."""
    X_196 = eval_trilinear_point(model, A, B, C, '(cos(B) + cos(C) - cos(A) - 1)*sec(A)*tan(A/2)', ID="X(196)", classes=["center"])
    X_268 = isogonal_conjugate(model, A, B, C, X_196, ID="X(268)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_3, X_9, 3, 9, incident=True)
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X(219)", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '1 + cos(2*A)', ID="X(255)", classes=["center", "incident"])
    central_line(model, X_219, X_255, 219, 255, incident=True)
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X(21)", classes=["center", "incident"])
    X_280 = point_from_barycentrics(model, A, B, C, -0.15770609, -0.1827957, 1.3405018, ID="X(280)", classes=["center", "incident"])
    central_line(model, X_21, X_280, 21, 280, incident=True)
    return promote_point_to_top(model, X_268)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(268) on the given reference triangle."""
    model = create_model('X(268) = ISOGONAL CONJUGATE OF X(196)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00268(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00268.json"))
    write_center_svg(
        model_acute,
        here / "x-00268.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
