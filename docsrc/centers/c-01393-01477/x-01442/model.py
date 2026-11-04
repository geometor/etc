"""GEOMETOR construction model for X_1442 = X_319-BETH CONJUGATE OF X_319."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01442(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1442 = X_319-BETH CONJUGATE OF X_319 on reference triangle ABC."""
    X_1442 = eval_trilinear_point(model, A, B, C, '((1 + 2*cos(A))/(1 + cos(A)))', ID="X_1442", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    central_line(model, X_1, X_7, 1, 7, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_326 = eval_trilinear_point(model, A, B, C, '(cot(A))**(2)', ID="X_326", classes=["center", "incident"])
    central_line(model, X_8, X_326, 8, 326, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X_651", classes=["center", "incident"])
    central_line(model, X_37, X_651, 37, 651, incident=True)
    return promote_point_to_top(model, X_1442)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1442 on the given reference triangle."""
    model = create_model('X_1442 = X_319-BETH CONJUGATE OF X_319')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01442(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01442.json"))
    write_center_svg(
        model_acute,
        here / "x-01442.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
