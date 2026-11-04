"""GEOMETOR construction model for X_1866 = ZOSMA TRANSFORM OF X_355."""

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
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01866(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1866 = ZOSMA TRANSFORM OF X_355 on reference triangle ABC."""
    X_28 = eval_trilinear_point(model, A, B, C, '(tan(A))/(b + c)', ID="X_28", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center"])
    X_80 = eval_trilinear_point(model, A, B, C, '1/(1 - 2*cos(A))', ID="X_80", classes=["center"])
    central_line(model, X_28, X_34, 28, 34)
    central_line(model, X_4, X_80, 4, 80)
    X_1866 = intersect_lines(model, X_28, X_34, X_4, X_80, ID="X_1866", classes=["selected", "target"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X_65", classes=["center", "incident"])
    central_line(model, X_51, X_65, 51, 65, incident=True)
    return promote_point_to_top(model, X_1866)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1866 on the given reference triangle."""
    model = create_model('X_1866 = ZOSMA TRANSFORM OF X_355')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01866(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01866.json"))
    write_center_svg(
        model_acute,
        here / "x-01866.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
