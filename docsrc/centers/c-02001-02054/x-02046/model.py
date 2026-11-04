"""GEOMETOR construction model for X_2046 = 6th EULER-VECTEN-GIBERT POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02046(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2046 = 6th EULER-VECTEN-GIBERT POINT on reference triangle ABC."""
    X_2046 = eval_trilinear_point(model, A, B, C, '(b*c*(- 2*(b**(2) - c**(2))**(2) + a**(2)*(3*b**(2) + 3*c**(2) - a**(2)) - 3**(1/2)*((b**(2) - c**(2))**(2) - a**(2)*(b**(2) + c**(2)))))', ID="X_2046", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A +  pi  /6)', ID="X_17", classes=["center", "incident"])
    X_486 = eval_trilinear_point(model, A, B, C, 'sec(A +  pi  /4)', ID="X_486", classes=["center", "incident"])
    central_line(model, X_17, X_486, 17, 486, incident=True)
    X_18 = eval_trilinear_point(model, A, B, C, 'csc(A -  pi  /6)', ID="X_18", classes=["center", "incident"])
    X_485 = eval_trilinear_point(model, A, B, C, 'sec(A -  pi  /4)', ID="X_485", classes=["center", "incident"])
    central_line(model, X_18, X_485, 18, 485, incident=True)
    return promote_point_to_top(model, X_2046)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2046 on the given reference triangle."""
    model = create_model('X_2046 = 6th EULER-VECTEN-GIBERT POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02046(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02046.json"))
    write_center_svg(
        model_acute,
        here / "x-02046.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
