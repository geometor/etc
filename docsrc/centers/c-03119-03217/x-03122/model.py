"""GEOMETOR construction model for X_3122 = DANNEELS PERSPECTOR FOR X_42."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03122(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3122 = DANNEELS PERSPECTOR FOR X_42 on reference triangle ABC."""
    X_3122 = eval_trilinear_point(model, A, B, C, '(a*(b + c)*(b - c)**(2))', ID="X_3122", classes=["selected", "target"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_244 = eval_trilinear_point(model, A, B, C, '(b - c)**(2)', ID="X_244", classes=["center", "incident"])
    central_line(model, X_11, X_244, 11, 244, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_86, X_256, 86, 256, incident=True)
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    X_291 = eval_trilinear_point(model, A, B, C, '1/(a**(2) - b*c)', ID="X_291", classes=["center", "incident"])
    central_line(model, X_190, X_291, 190, 291, incident=True)
    return promote_point_to_top(model, X_3122)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3122 on the given reference triangle."""
    model = create_model('X_3122 = DANNEELS PERSPECTOR FOR X_42')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03122(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03122.json"))
    write_center_svg(
        model_acute,
        here / "x-03122.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
