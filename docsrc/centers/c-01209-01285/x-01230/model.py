"""GEOMETOR construction model for X_1230 = ISOTOMIC CONJUGATE OF X_1171."""

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
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01230(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1230 = ISOTOMIC CONJUGATE OF X_1171 on reference triangle ABC."""
    X_1171 = eval_trilinear_point(model, A, B, C, 'a/((b + c)*(2*a + b + c))', ID="X_1171", classes=["center"])
    X_1230 = isotomic_conjugate(model, A, B, C, X_1171, ID="X_1230", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_2, X_39, 2, 39, incident=True)
    X_313 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(3)*c**(3)', ID="X_313", classes=["center", "incident"])
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    central_line(model, X_313, X_321, 313, 321, incident=True)
    X_339 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A))/a**(4)', ID="X_339", classes=["center", "incident"])
    X_440 = point_from_barycentrics(model, A, B, C, 0.44199278, 0.40077713, 0.15723009, ID="X_440", classes=["center", "incident"])
    central_line(model, X_339, X_440, 339, 440, incident=True)
    return promote_point_to_top(model, X_1230)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1230 on the given reference triangle."""
    model = create_model('X_1230 = ISOTOMIC CONJUGATE OF X_1171')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01230(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01230.json"))
    write_center_svg(
        model_acute,
        here / "x-01230.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
