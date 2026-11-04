"""GEOMETOR construction model for X_2669 = CROSSDIFFERENCE OF PU(85)."""

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
)
from geometor.etc.render import write_center_svg


def construct_x_02669(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2669 = CROSSDIFFERENCE OF PU(85) on reference triangle ABC."""
    X_2107 = eval_trilinear_point(model, A, B, C, '(a/((a + b)*(a + c)*(b**(2)*c**(2) - a**(2)*b**(2) - a**(2)*c**(2) + a*b*c*(b + c - a))))', ID="X_2107", classes=["center"])
    X_2669 = isogonal_conjugate(model, A, B, C, X_2107, ID="X_2669", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    central_line(model, X_1, X_75, 1, 75, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_99, X_238, 99, 238, incident=True)
    X_42 = eval_trilinear_point(model, A, B, C, 'a*(b + c)', ID="X_42", classes=["center", "incident"])
    X_873 = eval_trilinear_point(model, A, B, C, '(a*(b + c)) **(-2)', ID="X_873", classes=["center", "incident"])
    central_line(model, X_42, X_873, 42, 873, incident=True)
    return promote_point_to_top(model, X_2669)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2669 on the given reference triangle."""
    model = create_model('X_2669 = CROSSDIFFERENCE OF PU(85)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02669(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02669.json"))
    write_center_svg(
        model_acute,
        here / "x-02669.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
