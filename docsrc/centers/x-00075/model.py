"""GEOMETOR construction model for X(75) = ISOTOMIC CONJUGATE OF INCENTER."""

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
    gergonne_point_of,
    isogonal_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00075(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(75) = ISOTOMIC CONJUGATE OF INCENTER on reference triangle ABC."""
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center"])
    X_75 = isogonal_conjugate(model, A, B, C, X_31, ID="X(75)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    central_line(model, X_7, X_8, 7, 8, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    central_line(model, X_2, X_37, 2, 37, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center", "incident"])
    central_line(model, X_19, X_27, 19, 27, incident=True)
    return promote_point_to_top(model, X_75)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(75) on the given reference triangle."""
    model = create_model('X(75) = ISOTOMIC CONJUGATE OF INCENTER')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00075(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00075.json"))
    write_center_svg(
        model_acute,
        here / "x-00075.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
