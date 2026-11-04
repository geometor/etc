"""GEOMETOR construction model for X_1865 = ZOSMA TRANSFORM OF X_284."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01865(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1865 = ZOSMA TRANSFORM OF X_284 on reference triangle ABC."""
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_1859 = eval_trilinear_point(model, A, B, C, 'tan(A)*((b + c)*cos(A) + b*cos(B) + c*cos(C))', ID="X_1859", classes=["center"])
    X_1865 = ceva_conjugate(model, A, B, C, X_4, X_1859, ID="X_1865", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_12 = eval_trilinear_point(model, A, B, C, '1 + cos(B - C)', ID="X_12", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    central_line(model, X_12, X_37, 12, 37, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_407 = point_from_barycentrics(model, A, B, C, 0.10813862, 0.19355731, 0.69830407, ID="X_407", classes=["center", "incident"])
    central_line(model, X_19, X_407, 19, 407, incident=True)
    return promote_point_to_top(model, X_1865)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1865 on the given reference triangle."""
    model = create_model('X_1865 = ZOSMA TRANSFORM OF X_284')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01865(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01865.json"))
    write_center_svg(
        model_acute,
        here / "x-01865.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
