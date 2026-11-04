"""GEOMETOR construction model for X_1839 = ZOSMA TRANSFORM OF X_37."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01839(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1839 = ZOSMA TRANSFORM OF X_37 on reference triangle ABC."""
    X_1796 = point_from_barycentrics(model, A, B, C, 0.44749937, 0.39111445, 0.16138617, ID="X_1796", classes=["center"])
    X_1839 = isogonal_conjugate(model, A, B, C, X_1796, ID="X_1839", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_27, X_86, 27, 86, incident=True)
    X_225 = eval_trilinear_point(model, A, B, C, '(sec(A))*(cos(B) + cos(C))', ID="X_225", classes=["center", "incident"])
    X_608 = eval_trilinear_point(model, A, B, C, 'a*(1 - sec(A))', ID="X_608", classes=["center", "incident"])
    central_line(model, X_225, X_608, 225, 608, incident=True)
    return promote_point_to_top(model, X_1839)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1839 on the given reference triangle."""
    model = create_model('X_1839 = ZOSMA TRANSFORM OF X_37')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01839(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01839.json"))
    write_center_svg(
        model_acute,
        here / "x-01839.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
