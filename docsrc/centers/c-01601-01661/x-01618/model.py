"""GEOMETOR construction model for X_1618 = TCC-PERSPECTOR OF X_59."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_01618(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1618 = TCC-PERSPECTOR OF X_59 on reference triangle ABC."""
    X_59 = eval_trilinear_point(model, A, B, C, '1/(1 - cos(B - C))', ID="X_59", classes=["center"])
    X_692 = eval_trilinear_point(model, A, B, C, 'a**(2)/(b - c)', ID="X_692", classes=["center"])
    X_1618 = reflection_in_point(model, X_59, X_692, ID="X_1618", classes=["selected", "target"], guide=False)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    X_901 = eval_trilinear_point(model, A, B, C, 'a/((b - c)*(b + c - 2*a))', ID="X_901", classes=["center", "incident"])
    central_line(model, X_110, X_901, 110, 901, incident=True)
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X_651", classes=["center", "incident"])
    central_line(model, X_513, X_651, 513, 651, incident=True)
    X_109 = eval_trilinear_point(model, A, B, C, 'a/(cos(B) - cos(C))', ID="X_109", classes=["center", "incident"])
    X_1459 = eval_trilinear_point(model, A, B, C, '(b - c)*cos(A)', ID="X_1459", classes=["center", "incident"])
    central_line(model, X_109, X_1459, 109, 1459, incident=True)
    return promote_point_to_top(model, X_1618)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1618 on the given reference triangle."""
    model = create_model('X_1618 = TCC-PERSPECTOR OF X_59')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01618(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01618.json"))
    write_center_svg(
        model_acute,
        here / "x-01618.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
