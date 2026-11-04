"""GEOMETOR construction model for X_2965 = BARYCENTRIC PRODUCT X_61*X_62."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02965(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2965 = BARYCENTRIC PRODUCT X_61*X_62 on reference triangle ABC."""
    X_2965 = eval_trilinear_point(model, A, B, C, 'sin(A)*sin(A +  pi  /6)*sin(A -  pi  /6)', ID="X_2965", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    central_line(model, X_53, X_112, 53, 112, incident=True)
    X_524 = eval_trilinear_point(model, A, B, C, '(2*a**(2) - b**(2) - c**(2))/a', ID="X_524", classes=["center", "incident"])
    X_1238 = point_from_barycentrics(model, A, B, C, 0.61143196, 0.31562453, 0.072943511, ID="X_1238", classes=["center", "incident"])
    central_line(model, X_524, X_1238, 524, 1238, incident=True)
    return promote_point_to_top(model, X_2965)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2965 on the given reference triangle."""
    model = create_model('X_2965 = BARYCENTRIC PRODUCT X_61*X_62')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02965(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02965.json"))
    write_center_svg(
        model_acute,
        here / "x-02965.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
