"""GEOMETOR construction model for X_3557 = 1st PAPPUS POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03557(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3557 = 1st PAPPUS POINT on reference triangle ABC."""
    X_3557 = eval_trilinear_point(model, A, B, C, 'e*sin(A) + sin(A -  omega  )', ID="X_3557", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_3414 = eval_trilinear_point(model, A, B, C, '1/(e*cos(A) + cos(A +  omega  ))', ID="X_3414", classes=["center", "incident"])
    central_line(model, X_4, X_3414, 4, 3414, incident=True)
    X_194 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*b**(2) + a**(2)*c**(2) - b**(2)*c**(2))', ID="X_194", classes=["center", "incident"])
    X_3413 = eval_trilinear_point(model, A, B, C, '1/(e*cos(A) - cos(A +  omega  ))', ID="X_3413", classes=["center", "incident"])
    central_line(model, X_194, X_3413, 194, 3413, incident=True)
    return promote_point_to_top(model, X_3557)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3557 on the given reference triangle."""
    model = create_model('X_3557 = 1st PAPPUS POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03557(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03557.json"))
    write_center_svg(
        model_acute,
        here / "x-03557.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
