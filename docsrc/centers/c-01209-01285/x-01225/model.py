"""GEOMETOR construction model for X_1225 = ISOTOMIC CONJUGATE OF X_1166."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01225(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1225 = ISOTOMIC CONJUGATE OF X_1166 on reference triangle ABC."""
    X_1166 = point_from_barycentrics(model, A, B, C, 0.20424736, 0.33803917, 0.45771347, ID="X_1166", classes=["center"])
    X_1225 = isotomic_conjugate(model, A, B, C, X_1166, ID="X_1225", classes=["selected", "target"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X_95", classes=["center", "incident"])
    central_line(model, X_76, X_95, 76, 95, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_311 = eval_trilinear_point(model, A, B, C, '(csc(A))**(2)*cos(B - C)', ID="X_311", classes=["center", "incident"])
    central_line(model, X_5, X_311, 5, 311, incident=True)
    X_339 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A))/a**(4)', ID="X_339", classes=["center", "incident"])
    X_1232 = point_from_barycentrics(model, A, B, C, 0.47795093, 0.32307014, 0.19897893, ID="X_1232", classes=["center", "incident"])
    central_line(model, X_339, X_1232, 339, 1232, incident=True)
    return promote_point_to_top(model, X_1225)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1225 on the given reference triangle."""
    model = create_model('X_1225 = ISOTOMIC CONJUGATE OF X_1166')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01225(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01225.json"))
    write_center_svg(
        model_acute,
        here / "x-01225.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
