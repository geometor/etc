"""GEOMETOR construction model for X(43) = X(6)-CEVA CONJUGATE OF X(1)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00043(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(43) = X(6)-CEVA CONJUGATE OF X(1) on reference triangle ABC."""
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X(43)", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X(87)", classes=["center", "incident"])
    central_line(model, X_6, X_87, 6, 87, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    central_line(model, X_31, X_100, 31, 100, incident=True)
    return promote_point_to_top(model, X_43)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(43) on the given reference triangle."""
    model = create_model('X(43) = X(6)-CEVA CONJUGATE OF X(1)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00043(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00043.json"))
    write_center_svg(
        model_acute,
        here / "x-00043.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
