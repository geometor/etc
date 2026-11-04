"""GEOMETOR construction model for X_1456 = X_516-BETH CONJUGATE OF X_516."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01456(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1456 = X_516-BETH CONJUGATE OF X_516 on reference triangle ABC."""
    X_105 = eval_trilinear_point(model, A, B, C, '1/(b**(2) + c**(2) - a*(b + c))', ID="X_105", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_1456 = ceva_conjugate(model, A, B, C, X_105, X_56, ID="X_1456", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    X_223 = eval_trilinear_point(model, A, B, C, '(tan(A/2))*(cos(B) + cos(C) - cos(A) - 1)', ID="X_223", classes=["center", "incident"])
    central_line(model, X_55, X_223, 55, 223, incident=True)
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center", "incident"])
    central_line(model, X_56, X_269, 56, 269, incident=True)
    return promote_point_to_top(model, X_1456)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1456 on the given reference triangle."""
    model = create_model('X_1456 = X_516-BETH CONJUGATE OF X_516')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01456(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01456.json"))
    write_center_svg(
        model_acute,
        here / "x-01456.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
