"""GEOMETOR construction model for X_2114 = POINT KEPLER V."""

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
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02114(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2114 = POINT KEPLER V on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    central_line(model, X_9, X_77, 9, 77)
    central_line(model, X_31, X_57, 31, 57)
    X_2114 = intersect_lines(model, X_9, X_77, X_31, X_57, ID="X_2114", classes=["selected", "target"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center", "incident"])
    central_line(model, X_238, X_241, 238, 241, incident=True)
    return promote_point_to_top(model, X_2114)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2114 on the given reference triangle."""
    model = create_model('X_2114 = POINT KEPLER V')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02114(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02114.json"))
    write_center_svg(
        model_acute,
        here / "x-02114.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
