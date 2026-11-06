"""GEOMETOR construction model for X_3497 = ISOGONAL CONJUGATE OF X_3496."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03497(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3497 = ISOGONAL CONJUGATE OF X_3496 on reference triangle ABC."""
    X_3496 = eval_trilinear_point(model, A, B, C, '(b**(3) + c**(3) - a**(3) + a*b*c)', ID="X_3496", classes=["center"])
    X_3497 = isogonal_conjugate(model, A, B, C, X_3496, ID="X_3497", classes=["selected", "target"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    X_384 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(4) + b**(2)*c**(2))', ID="X_384", classes=["center", "incident"])
    central_line(model, X_257, X_384, 257, 384, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_984 = eval_trilinear_point(model, A, B, C, 'b**(2) + b*c + c**(2)', ID="X_984", classes=["center", "incident"])
    central_line(model, X_3, X_984, 3, 984, incident=True)
    X_607 = eval_trilinear_point(model, A, B, C, 'a*(1 + sec(A))', ID="X_607", classes=["center", "incident"])
    X_2221 = point_from_barycentrics(model, A, B, C, 0.20882469, 0.32409591, 0.4670794, ID="X_2221", classes=["center", "incident"])
    central_line(model, X_607, X_2221, 607, 2221, incident=True)
    return promote_point_to_top(model, X_3497)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3497 on the given reference triangle."""
    model = create_model('X_3497 = ISOGONAL CONJUGATE OF X_3496')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03497(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03497.json"))
    write_center_svg(
        model_acute,
        here / "x-03497.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
