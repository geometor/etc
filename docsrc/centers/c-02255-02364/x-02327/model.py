"""GEOMETOR construction model for X_2327 = X_2-ISOCONJUGATE OF (1426)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02327(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2327 = X_2-ISOCONJUGATE OF (1426) on reference triangle ABC."""
    X_1792 = point_from_barycentrics(model, A, B, C, 0.64689234, 0.29959202, 0.053515639, ID="X_1792", classes=["center"])
    X_1812 = eval_trilinear_point(model, A, B, C, 'cot(A)*cot(A/2)/(b + c)', ID="X_1812", classes=["center"])
    X_2327 = crosspoint(model, A, B, C, X_1792, X_1812, ID="X_2327", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_9, X_21, 9, 21, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    central_line(model, X_48, X_63, 48, 63, incident=True)
    X_219 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A/2)', ID="X_219", classes=["center", "incident"])
    X_283 = eval_trilinear_point(model, A, B, C, '(cos(A))/(cos(B) + cos(C))', ID="X_283", classes=["center", "incident"])
    central_line(model, X_219, X_283, 219, 283, incident=True)
    return promote_point_to_top(model, X_2327)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2327 on the given reference triangle."""
    model = create_model('X_2327 = X_2-ISOCONJUGATE OF (1426)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02327(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02327.json"))
    write_center_svg(
        model_acute,
        here / "x-02327.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
