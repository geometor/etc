"""GEOMETOR construction model for X(263) = ISOGONAL CONJUGATE OF X(183)."""

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
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00263(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(263) = ISOGONAL CONJUGATE OF X(183) on reference triangle ABC."""
    X_183 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*cos(A- omega )', ID="X(183)", classes=["center"])
    X_263 = isogonal_conjugate(model, A, B, C, X_183, ID="X(263)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X(51)", classes=["center", "incident"])
    central_line(model, X_2, X_51, 2, 51, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_160 = point_from_barycentrics(model, A, B, C, 0.55772762, 0.55017141, -0.10789903, ID="X(160)", classes=["center", "incident"])
    central_line(model, X_6, X_160, 6, 160, incident=True)
    X_184 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(A)', ID="X(184)", classes=["center", "incident"])
    X_251 = eval_trilinear_point(model, A, B, C, 'a**(2)*csc(A + omega )', ID="X(251)", classes=["center", "incident"])
    central_line(model, X_184, X_251, 184, 251, incident=True)
    return promote_point_to_top(model, X_263)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(263) on the given reference triangle."""
    model = create_model('X(263) = ISOGONAL CONJUGATE OF X(183)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00263(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00263.json"))
    write_center_svg(
        model_acute,
        here / "x-00263.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
