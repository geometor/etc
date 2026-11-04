"""GEOMETOR construction model for X_2359 = X_2-ISOCONJUGATE OF X_1829."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02359(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2359 = X_2-ISOCONJUGATE OF X_1829 on reference triangle ABC."""
    X_1848 = point_from_barycentrics(model, A, B, C, 0.14011799, 0.21533923, 0.64454277, ID="X_1848", classes=["center"])
    X_2359 = isogonal_conjugate(model, A, B, C, X_1848, ID="X_2359", classes=["selected", "target"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X_78", classes=["center", "incident"])
    central_line(model, X_48, X_78, 48, 78, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_205 = eval_trilinear_point(model, A, B, C, '(a**(2)*(b**(2)*tan(B/2) + c**(2)*tan(C/2) - a**(2)*tan(A/2)))', ID="X_205", classes=["center", "incident"])
    central_line(model, X_9, X_205, 9, 205, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_284 = eval_trilinear_point(model, A, B, C, '(sin(A))/(cos(B) + cos(C))', ID="X_284", classes=["center", "incident"])
    central_line(model, X_42, X_284, 42, 284, incident=True)
    return promote_point_to_top(model, X_2359)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2359 on the given reference triangle."""
    model = create_model('X_2359 = X_2-ISOCONJUGATE OF X_1829')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02359(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02359.json"))
    write_center_svg(
        model_acute,
        here / "x-02359.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
