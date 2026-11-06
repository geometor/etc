"""GEOMETOR construction model for X_3749 = X_1707com[n(MEDIAL)*n(INCENTRAL)]."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03749(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3749 = X_1707com[n(MEDIAL)*n(INCENTRAL)] on reference triangle ABC."""
    X_3749 = eval_barycentric_point(model, A, B, C, '(a*(3*a**(2) + b**(2) + c**(2) - 2*a*b - 2*a*c))', ID="X_3749", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    central_line(model, X_1, X_3, 1, 3, incident=True)
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X_200", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_200, X_238, 200, 238, incident=True)
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X_100", classes=["center", "incident"])
    X_614 = eval_trilinear_point(model, A, B, C, 'a**(2) + b**(2) + c**(2) - 2*b*c', ID="X_614", classes=["center", "incident"])
    central_line(model, X_100, X_614, 100, 614, incident=True)
    return promote_point_to_top(model, X_3749)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3749 on the given reference triangle."""
    model = create_model('X_3749 = X_1707com[n(MEDIAL)*n(INCENTRAL)]')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03749(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03749.json"))
    write_center_svg(
        model_acute,
        here / "x-03749.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
