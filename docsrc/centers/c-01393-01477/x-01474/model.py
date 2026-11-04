"""GEOMETOR construction model for X_1474 = X_1172-BETH CONJUGATE OF X_1172."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01474(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1474 = X_1172-BETH CONJUGATE OF X_1172 on reference triangle ABC."""
    X_306 = eval_trilinear_point(model, A, B, C, '(b**(2)*c**(2))*(b + c)*cos(A)', ID="X_306", classes=["center"])
    X_1474 = isogonal_conjugate(model, A, B, C, X_306, ID="X_1474", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_1, X_19, 1, 19, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    central_line(model, X_6, X_25, 6, 25, incident=True)
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_27, X_86, 27, 86, incident=True)
    return promote_point_to_top(model, X_1474)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1474 on the given reference triangle."""
    model = create_model('X_1474 = X_1172-BETH CONJUGATE OF X_1172')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01474(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01474.json"))
    write_center_svg(
        model_acute,
        here / "x-01474.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
