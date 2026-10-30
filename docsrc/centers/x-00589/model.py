"""GEOMETOR construction model for X(589) = 2nd KENMOTU-VAN LAMOEN POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00589(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(589) = 2nd KENMOTU-VAN LAMOEN POINT on reference triangle ABC."""
    X_589 = point_from_barycentrics(model, A, B, C, 0.10099872, 0.21564339, 0.68335789, ID="X(589)", classes=["selected", "target"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X(39)", classes=["center", "incident"])
    X_588 = point_from_barycentrics(model, A, B, C, 0.26340212, 0.33528188, 0.401316, ID="X(588)", classes=["center", "incident"])
    central_line(model, X_39, X_588, 39, 588, incident=True)
    return promote_point_to_top(model, X_589)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(589) on the given reference triangle."""
    model = create_model('X(589) = 2nd KENMOTU-VAN LAMOEN POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00589(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00589.json"))
    write_center_svg(
        model_acute,
        here / "x-00589.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
