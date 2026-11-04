"""GEOMETOR construction model for X_1108 = CROSSPOINT OF X_2 AND X_84."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01108(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1108 = CROSSPOINT OF X_2 AND X_84 on reference triangle ABC."""
    X_322 = eval_trilinear_point(model, A, B, C, '((-1 - cos(A) + cos(B) + cos(C))*(csc(A))**(2))', ID="X_322", classes=["center"])
    X_1108 = complement(model, A, B, C, X_322, ID="X_1108", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_19, X_56, 19, 56, incident=True)
    X_104 = eval_trilinear_point(model, A, B, C, '1/(-1 + cos(B) + cos(C))', ID="X_104", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_104, X_112, 104, 112, incident=True)
    return promote_point_to_top(model, X_1108)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1108 on the given reference triangle."""
    model = create_model('X_1108 = CROSSPOINT OF X_2 AND X_84')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01108(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01108.json"))
    write_center_svg(
        model_acute,
        here / "x-01108.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
