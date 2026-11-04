"""GEOMETOR construction model for X_2799 = ISOGONAL CONJUGATE OF X_2715."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02799(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2799 = ISOGONAL CONJUGATE OF X_2715 on reference triangle ABC."""
    X_2715 = eval_trilinear_point(model, A, B, C, 'a/((b**(2) - c**(2))*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)))', ID="X_2715", classes=["center"])
    X_2799 = isogonal_conjugate(model, A, B, C, X_2715, ID="X_2799", classes=["selected", "target"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_99, X_112, 99, 112, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X_127", classes=["center", "incident"])
    central_line(model, X_115, X_127, 115, 127, incident=True)
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B +  omega  ) + c*sec(C +  omega  ))', ID="X_114", classes=["center", "incident"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X_132", classes=["center", "incident"])
    central_line(model, X_114, X_132, 114, 132, incident=True)
    return promote_point_to_top(model, X_2799)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2799 on the given reference triangle."""
    model = create_model('X_2799 = ISOGONAL CONJUGATE OF X_2715')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02799(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02799.json"))
    write_center_svg(
        model_acute,
        here / "x-02799.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
