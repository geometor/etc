"""GEOMETOR construction model for X(204) = X(1)-CEVA CONJUGATE OF X(19)."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00204(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(204) = X(1)-CEVA CONJUGATE OF X(19) on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center"])
    X_33 = eval_trilinear_point(model, A, B, C, '1 + sec(A)', ID="X(33)", classes=["center"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X(19)", classes=["center"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center"])
    central_line(model, X_6, X_33, 6, 33)
    central_line(model, X_19, X_31, 19, 31)
    X_204 = intersect_lines(model, X_6, X_33, X_19, X_31, ID="X(204)", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X(34)", classes=["center", "incident"])
    central_line(model, X_25, X_34, 25, 34, incident=True)
    return promote_point_to_top(model, X_204)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(204) on the given reference triangle."""
    model = create_model('X(204) = X(1)-CEVA CONJUGATE OF X(19)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00204(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00204.json"))
    write_center_svg(
        model_acute,
        here / "x-00204.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
