"""GEOMETOR construction model for X_2217 = X_2-ISOCONJUGATE OF X_573."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02217(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2217 = X_2-ISOCONJUGATE OF X_573 on reference triangle ABC."""
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    central_line(model, X_3, X_10, 3, 10)
    central_line(model, X_37, X_48, 37, 48)
    X_2217 = intersect_lines(model, X_3, X_10, X_37, X_48, ID="X_2217", classes=["selected", "target"])
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center", "incident"])
    X_158 = eval_trilinear_point(model, A, B, C, '(sec(A))**(2)', ID="X_158", classes=["center", "incident"])
    central_line(model, X_28, X_158, 28, 158, incident=True)
    return promote_point_to_top(model, X_2217)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2217 on the given reference triangle."""
    model = create_model('X_2217 = X_2-ISOCONJUGATE OF X_573')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02217(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02217.json"))
    write_center_svg(
        model_acute,
        here / "x-02217.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
