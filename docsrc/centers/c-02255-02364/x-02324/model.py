"""GEOMETOR construction model for X_2324 = X_2-ISOCONJUGATE OF X_1413."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02324(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2324 = X_2-ISOCONJUGATE OF X_1413 on reference triangle ABC."""
    X_1422 = point_from_barycentrics(model, A, B, C, -0.022661722, -0.056036259, 1.078698, ID="X_1422", classes=["center"])
    X_2324 = isogonal_conjugate(model, A, B, C, X_1422, ID="X_2324", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_1, X_6, 1, 6, incident=True)
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    X_144 = eval_trilinear_point(model, A, B, C, '(csc(A))*(tan(B/2) + tan(C/2) - tan(A/2))', ID="X_144", classes=["center", "incident"])
    central_line(model, X_77, X_144, 77, 144, incident=True)
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X_33", classes=["center", "incident"])
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X_200", classes=["center", "incident"])
    central_line(model, X_33, X_200, 33, 200, incident=True)
    return promote_point_to_top(model, X_2324)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2324 on the given reference triangle."""
    model = create_model('X_2324 = X_2-ISOCONJUGATE OF X_1413')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02324(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02324.json"))
    write_center_svg(
        model_acute,
        here / "x-02324.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
