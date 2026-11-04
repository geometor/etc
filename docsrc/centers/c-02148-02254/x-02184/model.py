"""GEOMETOR construction model for X_2184 = X_2-ISOCONJUGATE OF X_154."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02184(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2184 = X_2-ISOCONJUGATE OF X_154 on reference triangle ABC."""
    X_610 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C) - tan(A)', ID="X_610", classes=["center"])
    X_2184 = isogonal_conjugate(model, A, B, C, X_610, ID="X_2184", classes=["selected", "target"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center", "incident"])
    X_64 = eval_trilinear_point(model, A, B, C, '1/(cos(A) - cos(B)*cos(C))', ID="X_64", classes=["center", "incident"])
    central_line(model, X_40, X_64, 40, 64, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_204 = eval_trilinear_point(model, A, B, C, '((tan(A))*(tan(B) + tan(C) - tan(A)))', ID="X_204", classes=["center", "incident"])
    central_line(model, X_1, X_204, 1, 204, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    central_line(model, X_9, X_223, 9, 223, incident=True)
    return promote_point_to_top(model, X_2184)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2184 on the given reference triangle."""
    model = create_model('X_2184 = X_2-ISOCONJUGATE OF X_154')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02184(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02184.json"))
    write_center_svg(
        model_acute,
        here / "x-02184.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
