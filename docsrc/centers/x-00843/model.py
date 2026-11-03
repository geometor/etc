"""GEOMETOR construction model for X_843 = ISOGONAL CONJUGATE OF X_543."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_00843(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_843 = ISOGONAL CONJUGATE OF X_543 on reference triangle ABC."""
    X_352 = point_from_barycentrics(model, A, B, C, -2.5765986, 0.16705151, 3.4095471, ID="X_352", classes=["center"])
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X_187", classes=["center"])
    X_843 = reflection_in_point(model, X_352, X_187, ID="X_843", classes=["selected", "target"], guide=False)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_110, X_187, 110, 187, incident=True)
    X_111 = eval_trilinear_point(model, A, B, C, 'a/(2*a**(2) - b**(2) - c**(2))', ID="X_111", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_111, X_512, 111, 512, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_525 = eval_trilinear_point(model, A, B, C, '(b*cos(B) - c*cos(C))/a', ID="X_525", classes=["center", "incident"])
    central_line(model, X_99, X_525, 99, 525, incident=True)
    return promote_point_to_top(model, X_843)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_843 on the given reference triangle."""
    model = create_model('X_843 = ISOGONAL CONJUGATE OF X_543')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00843(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00843.json"))
    write_center_svg(
        model_acute,
        here / "x-00843.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
