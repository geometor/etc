"""GEOMETOR construction model for X_1722 = MIMOSA TRANSFORM OF X_56."""

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
    incenter_of,
    intersect_lines,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01722(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1722 = MIMOSA TRANSFORM OF X_56 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center"])
    X_40 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A) - 1', ID="X_40", classes=["center"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center"])
    central_line(model, X_1, X_2, 1, 2)
    central_line(model, X_40, X_238, 40, 238)
    X_1722 = intersect_lines(model, X_1, X_2, X_40, X_238, ID="X_1722", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_986 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + b*c + c**(2)) + b**(3) + c**(3))', ID="X_986", classes=["center", "incident"])
    central_line(model, X_9, X_986, 9, 986, incident=True)
    return promote_point_to_top(model, X_1722)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1722 on the given reference triangle."""
    model = create_model('X_1722 = MIMOSA TRANSFORM OF X_56')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01722(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01722.json"))
    write_center_svg(
        model_acute,
        here / "x-01722.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
