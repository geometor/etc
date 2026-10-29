"""GEOMETOR construction model for X(837) = ISOGONAL CONJUGATE OF X(836)."""

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


def construct_x_00837(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(837) = ISOGONAL CONJUGATE OF X(836) on reference triangle ABC."""
    X_836 = point_from_barycentrics(model, A, B, C, 0.42530217, 0.48277516, 0.091922678, ID="X(836)", classes=["center"])
    X_837 = isogonal_conjugate(model, A, B, C, X_836, ID="X(837)", classes=["selected", "target"])
    X_393 = eval_trilinear_point(model, A, B, C, 'sec(A) - csc(B)*csc(C)', ID="X(393)", classes=["center", "incident"])
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X(394)", classes=["center", "incident"])
    central_line(model, X_393, X_394, 393, 394, incident=True)
    return promote_point_to_top(model, X_837)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(837) on the given reference triangle."""
    model = create_model('X(837) = ISOGONAL CONJUGATE OF X(836)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00837(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00837.json"))
    write_center_svg(
        model_acute,
        here / "x-00837.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
