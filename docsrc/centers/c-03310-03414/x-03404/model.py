"""GEOMETOR construction model for X_3404 = TAN(A + ω) POINT."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03404(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3404 = TAN(A + ω) POINT on reference triangle ABC."""
    X_3404 = eval_trilinear_point(model, A, B, C, '(tan(A +  omega  ))', ID="X_3404", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_163 = eval_trilinear_point(model, A, B, C, '(sin(2*A))/(sin(2*B) - sin(2*C))', ID="X_163", classes=["center", "incident"])
    central_line(model, X_1, X_163, 1, 163, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_561 = eval_trilinear_point(model, A, B, C, 'a **(- 4)', ID="X_561", classes=["center", "incident"])
    central_line(model, X_63, X_561, 63, 561, incident=True)
    X_2157 = point_from_barycentrics(model, A, B, C, 0.3595619, 1.1175611, -0.47712301, ID="X_2157", classes=["center", "incident"])
    X_2624 = eval_trilinear_point(model, A, B, C, 'cot(A - B) + cot(A - C)', ID="X_2624", classes=["center", "incident"])
    central_line(model, X_2157, X_2624, 2157, 2624, incident=True)
    return promote_point_to_top(model, X_3404)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3404 on the given reference triangle."""
    model = create_model('X_3404 = TAN(A + ω) POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03404(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03404.json"))
    write_center_svg(
        model_acute,
        here / "x-03404.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
