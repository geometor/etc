"""GEOMETOR construction model for X_837 = ISOGONAL CONJUGATE OF X_836."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00837(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_837 = ISOGONAL CONJUGATE OF X_836 on reference triangle ABC."""
    X_836 = eval_trilinear_point(model, A, B, C, '(sin(B)*(sec(B))**(2) + sin(C)*(sec(C))**(2))', ID="X_836", classes=["center"])
    X_837 = isogonal_conjugate(model, A, B, C, X_836, ID="X_837", classes=["selected", "target"])
    X_393 = eval_trilinear_point(model, A, B, C, 'b*c*(tan(A))**(2)', ID="X_393", classes=["center", "incident"])
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    central_line(model, X_393, X_394, 393, 394, incident=True)
    return promote_point_to_top(model, X_837)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_837 on the given reference triangle."""
    model = create_model('X_837 = ISOGONAL CONJUGATE OF X_836')
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
