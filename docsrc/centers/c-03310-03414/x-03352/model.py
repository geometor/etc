"""GEOMETOR construction model for X_3352 = ISOGONAL CONJUGATE OF X_3351."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    incenter_of,
    isogonal_conjugate,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03352(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3352 = ISOGONAL CONJUGATE OF X_3351 on reference triangle ABC."""
    X_3351 = point_from_barycentrics(model, A, B, C, 0.20257124, 0.3139591, 0.48346966, ID="X_3351", classes=["center"])
    X_3352 = isogonal_conjugate(model, A, B, C, X_3351, ID="X_3352", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_3341 = point_from_barycentrics(model, A, B, C, 0.05793173, 0.086051457, 0.85601681, ID="X_3341", classes=["center", "incident"])
    central_line(model, X_3, X_3341, 3, 3341, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3350 = point_from_barycentrics(model, A, B, C, 0.2476751, 0.33176068, 0.42056423, ID="X_3350", classes=["center", "incident"])
    central_line(model, X_1, X_3350, 1, 3350, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_3343 = point_from_barycentrics(model, A, B, C, 0.15926582, 0.25678823, 0.58394595, ID="X_3343", classes=["center", "incident"])
    central_line(model, X_9, X_3343, 9, 3343, incident=True)
    return promote_point_to_top(model, X_3352)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3352 on the given reference triangle."""
    model = create_model('X_3352 = ISOGONAL CONJUGATE OF X_3351')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03352(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03352.json"))
    write_center_svg(
        model_acute,
        here / "x-03352.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
