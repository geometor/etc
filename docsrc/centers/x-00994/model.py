"""GEOMETOR construction model for X(994) = ISOGONAL CONJUGATE OF X(993)."""

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


def construct_x_00994(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(994) = ISOGONAL CONJUGATE OF X(993) on reference triangle ABC."""
    X_993 = eval_trilinear_point(model, A, B, C, 'a**(3)- a*(b**(2)+ c**(2)) - b*c*(b + c)', ID="X(993)", classes=["center"])
    X_994 = isogonal_conjugate(model, A, B, C, X_993, ID="X(994)", classes=["selected", "target"])
    X_65 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C)', ID="X(65)", classes=["center", "incident"])
    X_386 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) + b*c + c*a + a*b)', ID="X(386)", classes=["center", "incident"])
    central_line(model, X_65, X_386, 65, 386, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X(37)", classes=["center", "incident"])
    X_517 = eval_trilinear_point(model, A, B, C, '-1 + cos(B) + cos(C)', ID="X(517)", classes=["center", "incident"])
    central_line(model, X_37, X_517, 37, 517, incident=True)
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    X_759 = eval_trilinear_point(model, A, B, C, '1/(a**(0)*(b**(3)+ c**(3)) - a**(2)*(b**(1)+ c**(1)))', ID="X(759)", classes=["center", "incident"])
    central_line(model, X_31, X_759, 31, 759, incident=True)
    return promote_point_to_top(model, X_994)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(994) on the given reference triangle."""
    model = create_model('X(994) = ISOGONAL CONJUGATE OF X(993)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00994(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00994.json"))
    write_center_svg(
        model_acute,
        here / "x-00994.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
