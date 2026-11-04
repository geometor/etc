"""GEOMETOR construction model for X_1148 = YIU-HATZIPOLAKIS POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01148(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1148 = YIU-HATZIPOLAKIS POINT on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1148 = ceva_conjugate(model, A, B, C, X_1, X_4, ID="X_1148", classes=["selected", "target"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_4, X_65, 4, 65, incident=True)
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    X_243 = eval_trilinear_point(model, A, B, C, '(sec(A))*((cos(A))**(2) - cos(B)*cos(C))', ID="X_243", classes=["center", "incident"])
    central_line(model, X_46, X_243, 46, 243, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_653 = eval_trilinear_point(model, A, B, C, '1/(sec(B) - sec(C))', ID="X_653", classes=["center", "incident"])
    central_line(model, X_3, X_653, 3, 653, incident=True)
    return promote_point_to_top(model, X_1148)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1148 on the given reference triangle."""
    model = create_model('X_1148 = YIU-HATZIPOLAKIS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01148(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01148.json"))
    write_center_svg(
        model_acute,
        here / "x-01148.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
