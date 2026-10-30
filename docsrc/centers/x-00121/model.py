"""GEOMETOR construction model for X(121) = X(106)-OF-MEDIAL-TRIANGLE."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    feuerbach_point_of,
    intersect_lines,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00121(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(121) = X(106)-OF-MEDIAL-TRIANGLE on reference triangle ABC."""
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X(106)", classes=["center"])
    central_line(model, X_10, X_11, 10, 11)
    central_line(model, X_2, X_106, 2, 106)
    X_121 = intersect_lines(model, X_10, X_11, X_2, X_106, ID="X(121)", classes=["selected", "target"])
    X_116 = eval_trilinear_point(model, A, B, C, 'b*c*((b - c)**(2)*(b**(2) + b*c + c**(2) - a*b - a*c))', ID="X(116)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_116, X_141, 116, 141, incident=True)
    return promote_point_to_top(model, X_121)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(121) on the given reference triangle."""
    model = create_model('X(121) = X(106)-OF-MEDIAL-TRIANGLE')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00121(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00121.json"))
    write_center_svg(
        model_acute,
        here / "x-00121.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
