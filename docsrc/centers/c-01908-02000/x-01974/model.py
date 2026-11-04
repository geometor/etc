"""GEOMETOR construction model for X_1974 = BARYCENTRIC PRODUCT OF PU(39)."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01974(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1974 = BARYCENTRIC PRODUCT OF PU(39) on reference triangle ABC."""
    X_305 = eval_trilinear_point(model, A, B, C, 'b**(4)*c**(4)*cos(A)', ID="X_305", classes=["center"])
    X_1974 = isogonal_conjugate(model, A, B, C, X_305, ID="X_1974", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    central_line(model, X_4, X_83, 4, 83, incident=True)
    X_66 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4))', ID="X_66", classes=["center", "incident"])
    X_125 = eval_trilinear_point(model, A, B, C, 'cos(A)*(sin(B - C))**(2)', ID="X_125", classes=["center", "incident"])
    central_line(model, X_66, X_125, 66, 125, incident=True)
    return promote_point_to_top(model, X_1974)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1974 on the given reference triangle."""
    model = create_model('X_1974 = BARYCENTRIC PRODUCT OF PU(39)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01974(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01974.json"))
    write_center_svg(
        model_acute,
        here / "x-01974.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
