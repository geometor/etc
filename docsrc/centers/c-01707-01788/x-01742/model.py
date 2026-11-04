"""GEOMETOR construction model for X_1742 = MIMOSA TRANSFORM OF X_212."""

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
    gergonne_point_of,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01742(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1742 = MIMOSA TRANSFORM OF X_212 on reference triangle ABC."""
    X_1742 = eval_trilinear_point(model, A, B, C, '(sec(B/2))**(2) + (sec(C/2))**(2) - (sec(A/2))**(2)', ID="X_1742", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    X_165 = eval_trilinear_point(model, A, B, C, 'tan(B/2) + tan(C/2) - tan(A/2)', ID="X_165", classes=["center", "incident"])
    central_line(model, X_43, X_165, 43, 165, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_3, X_238, 3, 238, incident=True)
    return promote_point_to_top(model, X_1742)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1742 on the given reference triangle."""
    model = create_model('X_1742 = MIMOSA TRANSFORM OF X_212')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01742(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01742.json"))
    write_center_svg(
        model_acute,
        here / "x-01742.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
