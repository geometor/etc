"""GEOMETOR construction model for X_3469 = ISOGONAL CONJUGATE OF X_3468."""

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
    incenter_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03469(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3469 = ISOGONAL CONJUGATE OF X_3468 on reference triangle ABC."""
    X_3468 = eval_trilinear_point(model, A, B, C, '2 - sec(A) + sec(B) + sec(C)', ID="X_3468", classes=["center"])
    X_3469 = isogonal_conjugate(model, A, B, C, X_3468, ID="X_3469", classes=["selected", "target"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    X_1745 = eval_trilinear_point(model, A, B, C, '(sec(B) + sec(C) - sec(A))', ID="X_1745", classes=["center", "incident"])
    central_line(model, X_77, X_1745, 77, 1745, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_3462 = point_from_barycentrics(model, A, B, C, 1.0069407, 1.1981673, -1.2051081, ID="X_3462", classes=["center", "incident"])
    central_line(model, X_1, X_3462, 1, 3462, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_3460 = point_from_barycentrics(model, A, B, C, 0.29060152, 0.26847785, 0.44092064, ID="X_3460", classes=["center", "incident"])
    central_line(model, X_3, X_3460, 3, 3460, incident=True)
    return promote_point_to_top(model, X_3469)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3469 on the given reference triangle."""
    model = create_model('X_3469 = ISOGONAL CONJUGATE OF X_3468')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03469(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03469.json"))
    write_center_svg(
        model_acute,
        here / "x-03469.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
