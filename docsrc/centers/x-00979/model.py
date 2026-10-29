"""GEOMETOR construction model for X(979) = X(8)-CROSS CONJUGATE OF X(1)."""

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
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00979(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(979) = X(8)-CROSS CONJUGATE OF X(1) on reference triangle ABC."""
    X_978 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c) + a*(b**(2) - b*c + c**(2)) - b*c*(b + c)', ID="X(978)", classes=["center"])
    X_979 = isogonal_conjugate(model, A, B, C, X_978, ID="X(979)", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X(87)", classes=["center", "incident"])
    central_line(model, X_10, X_87, 10, 87, incident=True)
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["center", "incident"])
    X_58 = eval_trilinear_point(model, A, B, C, 'a/(b + c)', ID="X(58)", classes=["center", "incident"])
    central_line(model, X_43, X_58, 43, 58, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X(56)", classes=["center", "incident"])
    central_line(model, X_56, X_978, 56, 978, incident=True)
    return promote_point_to_top(model, X_979)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(979) on the given reference triangle."""
    model = create_model('X(979) = X(8)-CROSS CONJUGATE OF X(1)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00979(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00979.json"))
    write_center_svg(
        model_acute,
        here / "x-00979.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
