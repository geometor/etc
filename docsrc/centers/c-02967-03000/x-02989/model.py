"""GEOMETOR construction model for X_2989 = DC(X_103)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02989(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2989 = DC(X_103) on reference triangle ABC."""
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_516 = eval_trilinear_point(model, A, B, C, 'b*c*((a - b)*cot(C) + (a - c)*cot(B))', ID="X_516", classes=["center"])
    X_2989 = cevapoint(model, A, B, C, X_6, X_516, ID="X_2989", classes=["selected", "target"])
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center", "incident"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X_110", classes=["center", "incident"])
    central_line(model, X_27, X_110, 27, 110, incident=True)
    X_273 = eval_trilinear_point(model, A, B, C, 'sec(A)*(sec(A/2))**(2)', ID="X_273", classes=["center", "incident"])
    X_651 = eval_trilinear_point(model, A, B, C, '1/(cos(B) - cos(C))', ID="X_651", classes=["center", "incident"])
    central_line(model, X_273, X_651, 273, 651, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_1331 = eval_trilinear_point(model, A, B, C, '(cos(A))/(b - c)', ID="X_1331", classes=["center", "incident"])
    central_line(model, X_2, X_1331, 2, 1331, incident=True)
    return promote_point_to_top(model, X_2989)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2989 on the given reference triangle."""
    model = create_model('X_2989 = DC(X_103)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02989(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02989.json"))
    write_center_svg(
        model_acute,
        here / "x-02989.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
