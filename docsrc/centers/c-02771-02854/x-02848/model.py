"""GEOMETOR construction model for X_2848 = ISOGONAL CONJUGATE OF X_2764."""

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


def construct_x_02848(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2848 = ISOGONAL CONJUGATE OF X_2764 on reference triangle ABC."""
    X_2764 = point_from_barycentrics(model, A, B, C, 0.081175309, -0.10111868, 1.0199434, ID="X_2764", classes=["center"])
    X_2848 = isogonal_conjugate(model, A, B, C, X_2764, ID="X_2848", classes=["selected", "target"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_107, X_112, 107, 112, incident=True)
    X_122 = eval_trilinear_point(model, A, B, C, '(b**(2) - c**(2))**(2)*(cos(A) - cos(B)*cos(C))*(cot(A))**(2)', ID="X_122", classes=["center", "incident"])
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X_127", classes=["center", "incident"])
    central_line(model, X_122, X_127, 122, 127, incident=True)
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X_132", classes=["center", "incident"])
    X_133 = eval_trilinear_point(model, A, B, C, '(sec(A))*((sin(2*B) - sin(2*C))**(2) + (sin(2*A))*(sin(2*B)) + (sin(2*A))*(sin(2*C)) - 2*(sin(2*B))*(sin(2*C)))*(2*sin(2*A) - sin(2*B) - sin(2*C))', ID="X_133", classes=["center", "incident"])
    central_line(model, X_132, X_133, 132, 133, incident=True)
    return promote_point_to_top(model, X_2848)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2848 on the given reference triangle."""
    model = create_model('X_2848 = ISOGONAL CONJUGATE OF X_2764')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02848(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02848.json"))
    write_center_svg(
        model_acute,
        here / "x-02848.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
