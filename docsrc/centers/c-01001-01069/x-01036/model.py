"""GEOMETOR construction model for X_1036 = ISOGONAL CONJUGATE OF X_388."""

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
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01036(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1036 = ISOGONAL CONJUGATE OF X_388 on reference triangle ABC."""
    X_388 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) + (b + c)**(2))/(b + c - a)', ID="X_388", classes=["center"])
    X_1036 = isogonal_conjugate(model, A, B, C, X_388, ID="X_1036", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_1, X_25, 1, 25, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_3, X_31, 3, 31, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    central_line(model, X_55, X_78, 55, 78, incident=True)
    return promote_point_to_top(model, X_1036)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1036 on the given reference triangle."""
    model = create_model('X_1036 = ISOGONAL CONJUGATE OF X_388')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01036(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01036.json"))
    write_center_svg(
        model_acute,
        here / "x-01036.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
