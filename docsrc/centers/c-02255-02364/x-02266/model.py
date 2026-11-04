"""GEOMETOR construction model for X_2266 = X_2-ISOCONJUGATE OF X_955."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02266(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2266 = X_2-ISOCONJUGATE OF X_955 on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    central_line(model, X_6, X_31, 6, 31)
    central_line(model, X_48, X_57, 48, 57)
    X_2266 = intersect_lines(model, X_6, X_31, X_48, X_57, ID="X_2266", classes=["selected", "target"])
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_41, X_65, 41, 65, incident=True)
    return promote_point_to_top(model, X_2266)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2266 on the given reference triangle."""
    model = create_model('X_2266 = X_2-ISOCONJUGATE OF X_955')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02266(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02266.json"))
    write_center_svg(
        model_acute,
        here / "x-02266.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
