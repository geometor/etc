"""GEOMETOR construction model for X_2900 = ORTHIC-ISOGONAL CONJUGATE OF X_9."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02900(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2900 = ORTHIC-ISOGONAL CONJUGATE OF X_9 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_2900 = ceva_conjugate(model, A, B, C, X_4, X_9, ID="X_2900", classes=["selected", "target"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_9, X_55, 9, 55, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_442 = point_from_barycentrics(model, A, B, C, 0.3215734, 0.32603406, 0.35239254, ID="X_442", classes=["center", "incident"])
    central_line(model, X_1, X_442, 1, 442, incident=True)
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    X_950 = eval_trilinear_point(model, A, B, C, 'b*c*(b + c - a)*(2*a**(3) + (b + c)*(a**(2) + (b - c)**(2)))', ID="X_950", classes=["center", "incident"])
    central_line(model, X_78, X_950, 78, 950, incident=True)
    return promote_point_to_top(model, X_2900)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2900 on the given reference triangle."""
    model = create_model('X_2900 = ORTHIC-ISOGONAL CONJUGATE OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02900(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02900.json"))
    write_center_svg(
        model_acute,
        here / "x-02900.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
