"""GEOMETOR construction model for X(127) = X(112)-OF-MEDIAL-TRIANGLE."""

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
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00127(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(127) = X(112)-OF-MEDIAL-TRIANGLE on reference triangle ABC."""
    X_127 = eval_trilinear_point(model, A, B, C, 'b*c*(sin(2*B) - sin(2*C))*((b**(2) - c**(2))*sin(2*A) - b**(2)*sin(2*B) + c**(2)*sin(2*C))', ID="X(127)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X(112)", classes=["center", "incident"])
    central_line(model, X_2, X_112, 2, 112, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_114 = point_from_barycentrics(model, A, B, C, 0.37082211, -0.060960354, 0.69013825, ID="X(114)", classes=["center", "incident"])
    central_line(model, X_3, X_114, 3, 114, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_132 = point_from_barycentrics(model, A, B, C, 0.11002416, 0.049913231, 0.84006261, ID="X(132)", classes=["center", "incident"])
    central_line(model, X_5, X_132, 5, 132, incident=True)
    return promote_point_to_top(model, X_127)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(127) on the given reference triangle."""
    model = create_model('X(127) = X(112)-OF-MEDIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00127(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00127.json"))
    write_center_svg(
        model_acute,
        here / "x-00127.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
