"""GEOMETOR construction model for X_1716 = MIMOSA TRANSFORM OF X_31."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01716(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1716 = MIMOSA TRANSFORM OF X_31 on reference triangle ABC."""
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1716 = ceva_conjugate(model, A, B, C, X_25, X_1, ID="X_1716", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    central_line(model, X_9, X_43, 9, 43, incident=True)
    X_69 = eval_trilinear_point(model, A, B, C, '(cos(A))/a**(2)', ID="X_69", classes=["center", "incident"])
    central_line(model, X_1, X_69, 1, 69, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_3, X_238, 3, 238, incident=True)
    return promote_point_to_top(model, X_1716)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1716 on the given reference triangle."""
    model = create_model('X_1716 = MIMOSA TRANSFORM OF X_31')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01716(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01716.json"))
    write_center_svg(
        model_acute,
        here / "x-01716.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
