"""GEOMETOR construction model for X_2713 = SR(X_99, X_107)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    reflection_in_point,
)
from geometor.etc.render import write_center_svg


def construct_x_02713(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2713 = SR(X_99, X_107) on reference triangle ABC."""
    X_2706 = point_from_barycentrics(model, A, B, C, 1.0408365, 0.2875314, -0.32836793, ID="X_2706", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_2713 = reflection_in_point(model, X_2706, X_3, ID="X_2713", classes=["selected", "target"], guide=False)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_520 = eval_trilinear_point(model, A, B, C, '(cos(A))*(sin(2*B) - sin(2*C))', ID="X_520", classes=["center", "incident"])
    central_line(model, X_99, X_520, 99, 520, incident=True)
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_107, X_512, 107, 512, incident=True)
    X_511 = eval_trilinear_point(model, A, B, C, 'cos(A +  omega  )', ID="X_511", classes=["center", "incident"])
    X_1294 = eval_barycentric_point(model, A, B, C, '1/(a**(6)*(b**(2) + c**(2)) - a**(4)*(3*b**(4) - 4*b**(2)*c**(2) + 3*c**(4)) + 3*a**(2)*(b**(2) - c**(2))**(2)*(b**(2) + c**(2)) - (b**(2) - c**(2))**(2)*(b**(4) + 4*b**(2)*c**(2) + c**(4)))', ID="X_1294", classes=["center", "incident"])
    central_line(model, X_511, X_1294, 511, 1294, incident=True)
    return promote_point_to_top(model, X_2713)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2713 on the given reference triangle."""
    model = create_model('X_2713 = SR(X_99, X_107)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02713(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02713.json"))
    write_center_svg(
        model_acute,
        here / "x-02713.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
