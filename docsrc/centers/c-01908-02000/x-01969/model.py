"""GEOMETOR construction model for X_1969 = TRILINEAR PRODUCT OF PU(38)."""

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
    isotomic_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01969(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1969 = TRILINEAR PRODUCT OF PU(38) on reference triangle ABC."""
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_1969 = isotomic_conjugate(model, A, B, C, X_48, ID="X_1969", classes=["selected", "target"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_158 = eval_trilinear_point(model, A, B, C, '(sec(A))**(2)', ID="X_158", classes=["center", "incident"])
    central_line(model, X_75, X_158, 75, 158, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_336 = eval_trilinear_point(model, A, B, C, 'csc(A)*cot(A)*sec(A +  omega  )', ID="X_336", classes=["center", "incident"])
    central_line(model, X_1, X_336, 1, 336, incident=True)
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    X_304 = eval_trilinear_point(model, A, B, C, '(cot(A))*(csc(A))**(2)', ID="X_304", classes=["center", "incident"])
    central_line(model, X_92, X_304, 92, 304, incident=True)
    return promote_point_to_top(model, X_1969)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1969 on the given reference triangle."""
    model = create_model('X_1969 = TRILINEAR PRODUCT OF PU(38)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01969(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01969.json"))
    write_center_svg(
        model_acute,
        here / "x-01969.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
