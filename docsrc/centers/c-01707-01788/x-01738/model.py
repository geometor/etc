"""GEOMETOR construction model for X_1738 = MIMOSA TRANSFORM OF X_105."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01738(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1738 = MIMOSA TRANSFORM OF X_105 on reference triangle ABC."""
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center"])
    X_673 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2) - a*(b + c))', ID="X_673", classes=["center"])
    X_1738 = crosspoint(model, A, B, C, X_75, X_673, ID="X_1738", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_19, X_46, 19, 46, incident=True)
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    central_line(model, X_10, X_75, 10, 75, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    central_line(model, X_1, X_142, 1, 142, incident=True)
    return promote_point_to_top(model, X_1738)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1738 on the given reference triangle."""
    model = create_model('X_1738 = MIMOSA TRANSFORM OF X_105')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01738(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01738.json"))
    write_center_svg(
        model_acute,
        here / "x-01738.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
