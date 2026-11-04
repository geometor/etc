"""GEOMETOR construction model for X_1818 = INVERSE MIMOSA TRANSFORM OF X_1282."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01818(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1818 = INVERSE MIMOSA TRANSFORM OF X_1282 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_295 = eval_trilinear_point(model, A, B, C, '(cos(A))/(a**(2) - b*c)', ID="X_295", classes=["center"])
    X_1818 = crosspoint(model, A, B, C, X_3, X_295, ID="X_1818", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_3, X_48, 3, 48, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    central_line(model, X_69, X_73, 69, 73, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_142 = eval_trilinear_point(model, A, B, C, 'b + c - ((b - c)**(2))/a', ID="X_142", classes=["center", "incident"])
    central_line(model, X_1, X_142, 1, 142, incident=True)
    return promote_point_to_top(model, X_1818)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1818 on the given reference triangle."""
    model = create_model('X_1818 = INVERSE MIMOSA TRANSFORM OF X_1282')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01818(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01818.json"))
    write_center_svg(
        model_acute,
        here / "x-01818.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
