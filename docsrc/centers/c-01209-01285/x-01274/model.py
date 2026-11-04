"""GEOMETOR construction model for X_1274 = ISOTOMIC CONJUGATE OF X_1143."""

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
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01274(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1274 = ISOTOMIC CONJUGATE OF X_1143 on reference triangle ABC."""
    X_1143 = eval_trilinear_point(model, A, B, C, 'csc(A)*tan(A/4)', ID="X_1143", classes=["center"])
    X_1274 = isotomic_conjugate(model, A, B, C, X_1143, ID="X_1274", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X_177", classes=["center", "incident"])
    central_line(model, X_8, X_177, 8, 177, incident=True)
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X_174", classes=["center", "incident"])
    X_176 = eval_trilinear_point(model, A, B, C, '1 + sec(A/2)*cos(B/2)*cos(C/2)', ID="X_176", classes=["center", "incident"])
    central_line(model, X_174, X_176, 174, 176, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1489 = eval_trilinear_point(model, A, B, C, '((csc(A))*(1 - cos(A/2) - sin(A/2)))', ID="X_1489", classes=["center", "incident"])
    central_line(model, X_2, X_1489, 2, 1489, incident=True)
    return promote_point_to_top(model, X_1274)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1274 on the given reference triangle."""
    model = create_model('X_1274 = ISOTOMIC CONJUGATE OF X_1143')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01274(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01274.json"))
    write_center_svg(
        model_acute,
        here / "x-01274.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
