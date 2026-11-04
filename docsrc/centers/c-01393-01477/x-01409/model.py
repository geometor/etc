"""GEOMETOR construction model for X_1409 = X_71-BETH CONJUGATE OF X_71."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01409(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1409 = X_71-BETH CONJUGATE OF X_71 on reference triangle ABC."""
    X_1409 = eval_trilinear_point(model, A, B, C, 'a*(sec(B) + sec(C))', ID="X_1409", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_63, X_77, 63, 77, incident=True)
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    central_line(model, X_71, X_73, 71, 73, incident=True)
    return promote_point_to_top(model, X_1409)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1409 on the given reference triangle."""
    model = create_model('X_1409 = X_71-BETH CONJUGATE OF X_71')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01409(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01409.json"))
    write_center_svg(
        model_acute,
        here / "x-01409.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
