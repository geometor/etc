"""GEOMETOR construction model for X_1837 = ZOSMA TRANSFORM OF X_34."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01837(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1837 = ZOSMA TRANSFORM OF X_34 on reference triangle ABC."""
    X_1837 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - 2*cos(B)*cos(C)', ID="X_1837", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_1, X_5, 1, 5, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_10, X_55, 10, 55, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_4, X_65, 4, 65, incident=True)
    return promote_point_to_top(model, X_1837)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1837 on the given reference triangle."""
    model = create_model('X_1837 = ZOSMA TRANSFORM OF X_34')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01837(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01837.json"))
    write_center_svg(
        model_acute,
        here / "x-01837.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
