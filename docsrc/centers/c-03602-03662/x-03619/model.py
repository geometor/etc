"""GEOMETOR construction model for X_3619 = H(X_6; M, -1/2)."""

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
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03619(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3619 = H(X_6; M, -1/2) on reference triangle ABC."""
    X_3619 = eval_trilinear_point(model, A, B, C, '(b*c*(a**(2) + 3*b**(2) + 3*c**(2)))', ID="X_3619", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_631 = eval_trilinear_point(model, A, B, C, '2*cos(A) + cos(B)*cos(C)', ID="X_631", classes=["center", "incident"])
    X_1352 = eval_trilinear_point(model, A, B, C, 'a - 2*R*cos(B-C)*cot(omega) ', ID="X_1352", classes=["center", "incident"])
    central_line(model, X_631, X_1352, 631, 1352, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_3096 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) + b**(2)*c**(2) + c**(2)*a**(2) + a**(2)*b**(2))', ID="X_3096", classes=["center", "incident"])
    central_line(model, X_4, X_3096, 4, 3096, incident=True)
    return promote_point_to_top(model, X_3619)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3619 on the given reference triangle."""
    model = create_model('X_3619 = H(X_6; M, -1/2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03619(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03619.json"))
    write_center_svg(
        model_acute,
        here / "x-03619.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
