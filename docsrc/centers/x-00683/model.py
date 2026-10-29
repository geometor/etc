"""GEOMETOR construction model for X(683) = ISOGONAL CONJUGATE OF X(682)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00683(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(683) = ISOGONAL CONJUGATE OF X(682) on reference triangle ABC."""
    X_682 = point_from_barycentrics(model, A, B, C, 0.25664254, 0.47603357, 0.26732389, ID="X(682)", classes=["center"])
    X_683 = isogonal_conjugate(model, A, B, C, X_682, ID="X(683)", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X(25)", classes=["center", "incident"])
    X_305 = eval_trilinear_point(model, A, B, C, 'b**(4)*c**(4)*cos(A)', ID="X(305)", classes=["center", "incident"])
    central_line(model, X_25, X_305, 25, 305, incident=True)
    return promote_point_to_top(model, X_683)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(683) on the given reference triangle."""
    model = create_model('X(683) = ISOGONAL CONJUGATE OF X(682)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00683(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00683.json"))
    write_center_svg(
        model_acute,
        here / "x-00683.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
