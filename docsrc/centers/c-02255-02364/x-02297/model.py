"""GEOMETOR construction model for X_2297 = X_2-ISOCONJUGATE OF X_1191."""

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
    intersect_lines,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02297(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2297 = X_2-ISOCONJUGATE OF X_1191 on reference triangle ABC."""
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center"])
    X_200 = eval_trilinear_point(model, A, B, C, '(cot(A/2))**(2)', ID="X_200", classes=["center"])
    central_line(model, X_9, X_56, 9, 56)
    central_line(model, X_6, X_200, 6, 200)
    X_2297 = intersect_lines(model, X_9, X_56, X_6, X_200, ID="X_2297", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_269 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)', ID="X_269", classes=["center", "incident"])
    central_line(model, X_2, X_269, 2, 269, incident=True)
    return promote_point_to_top(model, X_2297)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2297 on the given reference triangle."""
    model = create_model('X_2297 = X_2-ISOCONJUGATE OF X_1191')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02297(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02297.json"))
    write_center_svg(
        model_acute,
        here / "x-02297.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
