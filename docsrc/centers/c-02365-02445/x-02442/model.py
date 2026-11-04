"""GEOMETOR construction model for X_2442 = ISOGONAL CONJUGATE OF X_2416."""

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
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02442(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2442 = ISOGONAL CONJUGATE OF X_2416 on reference triangle ABC."""
    X_2416 = point_from_barycentrics(model, A, B, C, 4.3751706, -3.2558729, -0.11929772, ID="X_2416", classes=["center"])
    X_2442 = isogonal_conjugate(model, A, B, C, X_2416, ID="X_2442", classes=["selected", "target"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_4, X_6, 4, 6, incident=True)
    X_112 = eval_trilinear_point(model, A, B, C, 'a/(sin(2*B) - sin(2*C))', ID="X_112", classes=["center", "incident"])
    X_1301 = point_from_barycentrics(model, A, B, C, -0.036707118, 0.057047829, 0.97965929, ID="X_1301", classes=["center", "incident"])
    central_line(model, X_112, X_1301, 112, 1301, incident=True)
    return promote_point_to_top(model, X_2442)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2442 on the given reference triangle."""
    model = create_model('X_2442 = ISOGONAL CONJUGATE OF X_2416')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02442(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02442.json"))
    write_center_svg(
        model_acute,
        here / "x-02442.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
