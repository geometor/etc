"""GEOMETOR construction model for X_3463 = ISOGONAL CONJUGATE OF X_3462."""

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
    isogonal_conjugate,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03463(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3463 = ISOGONAL CONJUGATE OF X_3462 on reference triangle ABC."""
    X_3462 = point_from_barycentrics(model, A, B, C, 1.0069407, 1.1981673, -1.2051081, ID="X_3462", classes=["center"])
    X_3463 = isogonal_conjugate(model, A, B, C, X_3462, ID="X_3463", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_2120 = point_from_barycentrics(model, A, B, C, 0.30475192, 0.22664215, 0.46860594, ID="X_2120", classes=["center", "incident"])
    central_line(model, X_3, X_2120, 3, 2120, incident=True)
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    central_line(model, X_5, X_3462, 5, 3462, incident=True)
    X_3460 = point_from_barycentrics(model, A, B, C, 0.29060152, 0.26847785, 0.44092064, ID="X_3460", classes=["center", "incident"])
    X_3468 = eval_trilinear_point(model, A, B, C, '2 - sec(A) + sec(B) + sec(C)', ID="X_3468", classes=["center", "incident"])
    central_line(model, X_3460, X_3468, 3460, 3468, incident=True)
    return promote_point_to_top(model, X_3463)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3463 on the given reference triangle."""
    model = create_model('X_3463 = ISOGONAL CONJUGATE OF X_3462')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03463(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03463.json"))
    write_center_svg(
        model_acute,
        here / "x-03463.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
