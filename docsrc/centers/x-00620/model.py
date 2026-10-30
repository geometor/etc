"""GEOMETOR construction model for X(620) = MIDPOINT OF X(618) AND X(619)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00620(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(620) = MIDPOINT OF X(618) AND X(619) on reference triangle ABC."""
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center"])
    X_620 = complement(model, A, B, C, X_115, ID="X(620)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(99)", classes=["center", "incident"])
    central_line(model, X_2, X_99, 2, 99, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_114 = eval_trilinear_point(model, A, B, C, 'b*c*(b*sec(B + omega ) + c*sec(C + omega ))', ID="X(114)", classes=["center", "incident"])
    central_line(model, X_3, X_114, 3, 114, incident=True)
    X_187 = eval_trilinear_point(model, A, B, C, 'a*(2*a**(2) - b**(2) - c**(2))', ID="X(187)", classes=["center", "incident"])
    X_325 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2))', ID="X(325)", classes=["center", "incident"])
    central_line(model, X_187, X_325, 187, 325, incident=True)
    return promote_point_to_top(model, X_620)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(620) on the given reference triangle."""
    model = create_model('X(620) = MIDPOINT OF X(618) AND X(619)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00620(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00620.json"))
    write_center_svg(
        model_acute,
        here / "x-00620.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
