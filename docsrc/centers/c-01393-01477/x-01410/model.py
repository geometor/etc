"""GEOMETOR construction model for X_1410 = X_73-BETH CONJUGATE OF X_73."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01410(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1410 = X_73-BETH CONJUGATE OF X_73 on reference triangle ABC."""
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_1042 = eval_trilinear_point(model, A, B, C, '((1 - cos(A))*(cos(B) + cos(C)))', ID="X_1042", classes=["center"])
    X_1410 = ceva_conjugate(model, A, B, C, X_56, X_1042, ID="X_1410", classes=["selected", "target"])
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center", "incident"])
    central_line(model, X_25, X_34, 25, 34, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_3, X_77, 3, 77, incident=True)
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    X_228 = eval_trilinear_point(model, A, B, C, '(sin(2*A))*(sin(B) + sin(C))', ID="X_228", classes=["center", "incident"])
    central_line(model, X_73, X_228, 73, 228, incident=True)
    return promote_point_to_top(model, X_1410)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1410 on the given reference triangle."""
    model = create_model('X_1410 = X_73-BETH CONJUGATE OF X_73')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01410(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01410.json"))
    write_center_svg(
        model_acute,
        here / "x-01410.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
