"""GEOMETOR construction model for X_1760 = MIMOSA TRANSFORM OF X_305."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01760(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1760 = MIMOSA TRANSFORM OF X_305 on reference triangle ABC."""
    X_1760 = eval_trilinear_point(model, A, B, C, '(a**(4) - b**(4) - c**(4))', ID="X_1760", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    central_line(model, X_19, X_27, 19, 27, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_82 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2))', ID="X_82", classes=["center", "incident"])
    central_line(model, X_1, X_82, 1, 82, incident=True)
    X_240 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(A +  omega  )', ID="X_240", classes=["center", "incident"])
    X_255 = eval_trilinear_point(model, A, B, C, '(cos(A))**(2)', ID="X_255", classes=["center", "incident"])
    central_line(model, X_240, X_255, 240, 255, incident=True)
    return promote_point_to_top(model, X_1760)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1760 on the given reference triangle."""
    model = create_model('X_1760 = MIMOSA TRANSFORM OF X_305')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01760(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01760.json"))
    write_center_svg(
        model_acute,
        here / "x-01760.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
