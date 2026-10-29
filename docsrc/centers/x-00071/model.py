"""GEOMETOR construction model for X(71) = ISOGONAL CONJUGATE OF X(27)."""

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
    isogonal_conjugate,
    mittenpunkt_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00071(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(71) = ISOGONAL CONJUGATE OF X(27) on reference triangle ABC."""
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X(27)", classes=["center"])
    X_71 = isogonal_conjugate(model, A, B, C, X_27, ID="X(71)", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    central_line(model, X_4, X_9, 4, 9, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X(48)", classes=["center", "incident"])
    central_line(model, X_3, X_48, 3, 48, incident=True)
    return promote_point_to_top(model, X_71)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(71) on the given reference triangle."""
    model = create_model('X(71) = ISOGONAL CONJUGATE OF X(27)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00071(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00071.json"))
    write_center_svg(
        model_acute,
        here / "x-00071.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
