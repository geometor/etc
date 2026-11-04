"""GEOMETOR construction model for X_1884 = ZOSMA TRANSFORM OF X_758."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01884(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1884 = ZOSMA TRANSFORM OF X_758 on reference triangle ABC."""
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center"])
    X_34 = eval_trilinear_point(model, A, B, C, '1 - sec(A)', ID="X_34", classes=["center"])
    X_1464 = eval_trilinear_point(model, A, B, C, '(1 - cos(A))*(b + c)*(b**(2) + c**(2) - a**(2) - b*c)', ID="X_1464", classes=["center"])
    central_line(model, X_2, X_3, 2, 3)
    central_line(model, X_34, X_1464, 34, 1464)
    X_1884 = intersect_lines(model, X_2, X_3, X_34, X_1464, ID="X_1884", classes=["selected", "target"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    X_1835 = point_from_barycentrics(model, A, B, C, -0.095625242, -0.037166086, 1.1327913, ID="X_1835", classes=["center", "incident"])
    central_line(model, X_513, X_1835, 513, 1835, incident=True)
    return promote_point_to_top(model, X_1884)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1884 on the given reference triangle."""
    model = create_model('X_1884 = ZOSMA TRANSFORM OF X_758')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01884(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01884.json"))
    write_center_svg(
        model_acute,
        here / "x-01884.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
