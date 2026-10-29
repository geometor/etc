"""GEOMETOR construction model for X(903) = X(1)-BLAIKIE TRANSFORM OF X(2)."""

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
    gergonne_point_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00903(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(903) = X(1)-BLAIKIE TRANSFORM OF X(2) on reference triangle ABC."""
    X_902 = eval_trilinear_point(model, A, B, C, 'a*(b + c - 2*a)', ID="X(902)", classes=["center"])
    X_903 = isogonal_conjugate(model, A, B, C, X_902, ID="X(903)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_45 = eval_trilinear_point(model, A, B, C, '2*b + 2*c - a', ID="X(45)", classes=["center", "incident"])
    central_line(model, X_2, X_45, 2, 45, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_86, X_99, 86, 99, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_528 = point_from_barycentrics(model, A, B, C, -0.26726124, 0.80178373, -0.53452248, ID="X(528)", classes=["center", "incident"])
    central_line(model, X_7, X_528, 7, 528, incident=True)
    return promote_point_to_top(model, X_903)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(903) on the given reference triangle."""
    model = create_model('X(903) = X(1)-BLAIKIE TRANSFORM OF X(2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00903(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00903.json"))
    write_center_svg(
        model_acute,
        here / "x-00903.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
