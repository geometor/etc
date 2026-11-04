"""GEOMETOR construction model for X_2270 = X_2-ISOCONJUGATE OF X_963."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02270(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2270 = X_2-ISOCONJUGATE OF X_963 on reference triangle ABC."""
    X_189 = eval_trilinear_point(model, A, B, C, 'b*c/(cos(B) + cos(C) - cos(A) - 1)', ID="X_189", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2270 = ceva_conjugate(model, A, B, C, X_189, X_1, ID="X_2270", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center", "incident"])
    central_line(model, X_6, X_57, 6, 57, incident=True)
    X_198 = eval_trilinear_point(model, A, B, C, '(a*(cos(B) + cos(C) - cos(A) - 1))', ID="X_198", classes=["center", "incident"])
    central_line(model, X_1, X_198, 1, 198, incident=True)
    return promote_point_to_top(model, X_2270)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2270 on the given reference triangle."""
    model = create_model('X_2270 = X_2-ISOCONJUGATE OF X_963')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02270(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02270.json"))
    write_center_svg(
        model_acute,
        here / "x-02270.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
