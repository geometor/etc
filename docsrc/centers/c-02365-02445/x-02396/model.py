"""GEOMETOR construction model for X_2396 = GIBERT-SIMSON TRANSFORM OF X_99."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02396(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2396 = GIBERT-SIMSON TRANSFORM OF X_99 on reference triangle ABC."""
    X_2396 = eval_barycentric_point(model, A, B, C, '(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))/(b**(2) - c**(2))', ID="X_2396", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_2, X_39, 2, 39, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_99, X_110, 99, 110, incident=True)
    X_325 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)', ID="X_325", classes=["center", "incident"])
    X_868 = eval_trilinear_point(model, A, B, C, 'sin(2*B)*sin(A - C)*csc(A - B) - sin(2*C)*sin(A - B)*csc(A - C)', ID="X_868", classes=["center", "incident"])
    central_line(model, X_325, X_868, 325, 868, incident=True)
    return promote_point_to_top(model, X_2396)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2396 on the given reference triangle."""
    model = create_model('X_2396 = GIBERT-SIMSON TRANSFORM OF X_99')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02396(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02396.json"))
    write_center_svg(
        model_acute,
        here / "x-02396.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
