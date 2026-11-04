"""GEOMETOR construction model for X_2507 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, GALLATLY CIRCLE}."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02507(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2507 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, GALLATLY CIRCLE} on reference triangle ABC."""
    X_2507 = eval_trilinear_point(model, A, B, C, '(a*((b**(4) - c**(4))*a**(6) - (b**(8) - c**(8))*a**(2) + 2*b**(4)*c**(4)*(b**(2) - c**(2))))', ID="X_2507", classes=["selected", "target"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_2024 = eval_trilinear_point(model, A, B, C, 'sin(A) - 3*sin(A - 2*omega  ) - 2*cos(omega)*sin(A + 3*omega  )', ID="X_2024", classes=["center", "incident"])
    central_line(model, X_512, X_2024, 512, 2024, incident=True)
    X_804 = eval_trilinear_point(model, A, B, C, 'a **(-3)*(b**(2) - c**(2)) + a**(1)*(b **(-2) - c **(-2))', ID="X_804", classes=["center", "incident"])
    X_2023 = eval_trilinear_point(model, A, B, C, '(sin(omega)*cos(B - C) - cos(2*omega)*sin(A +  omega  ))', ID="X_2023", classes=["center", "incident"])
    central_line(model, X_804, X_2023, 804, 2023, incident=True)
    X_1194 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) + c**(4) + a**(2)*b**(2) + a**(2)*c**(2)))', ID="X_1194", classes=["center", "incident"])
    X_1637 = eval_barycentric_point(model, A, B, C, 'tan(A)*(tan(B) - tan(C))*(tan(B) + tan(C) - 2*tan(A))', ID="X_1637", classes=["center", "incident"])
    central_line(model, X_1194, X_1637, 1194, 1637, incident=True)
    return promote_point_to_top(model, X_2507)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2507 on the given reference triangle."""
    model = create_model('X_2507 = RADICAL CENTER OF {NINE-POINT CIRCLE, 1st LEMOINE CIRCLE, GALLATLY CIRCLE}')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02507(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02507.json"))
    write_center_svg(
        model_acute,
        here / "x-02507.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
