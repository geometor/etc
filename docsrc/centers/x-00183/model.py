"""GEOMETOR construction model for X(183) = TRILINEAR PRODUCT X(75)X(182)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00183(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(183) = TRILINEAR PRODUCT X(75)X(182) on reference triangle ABC."""
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A- omega )', ID="X(183)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_3, X_76, 3, 76, incident=True)
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X(22)", classes=["center", "incident"])
    X_157 = point_from_barycentrics(model, A, B, C, 0.22698945, 0.13751531, 0.63549524, ID="X(157)", classes=["center", "incident"])
    central_line(model, X_22, X_157, 22, 157, incident=True)
    return promote_point_to_top(model, X_183)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(183) on the given reference triangle."""
    model = create_model('X(183) = TRILINEAR PRODUCT X(75)X(182)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00183(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00183.json"))
    write_center_svg(
        model_acute,
        here / "x-00183.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
