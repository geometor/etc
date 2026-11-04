"""GEOMETOR construction model for X_987 = ISOGONAL CONJUGATE OF X_986."""

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
    mittenpunkt_of,
    nagel_point_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00987(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_987 = ISOGONAL CONJUGATE OF X_986 on reference triangle ABC."""
    X_986 = eval_trilinear_point(model, A, B, C, '(a*(b**(2) + b*c + c**(2)) + b**(3) + c**(3))', ID="X_986", classes=["center"])
    X_987 = isogonal_conjugate(model, A, B, C, X_986, ID="X_987", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_8, X_31, 8, 31, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    central_line(model, X_9, X_32, 9, 32, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X_171", classes=["center", "incident"])
    central_line(model, X_4, X_171, 4, 171, incident=True)
    return promote_point_to_top(model, X_987)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_987 on the given reference triangle."""
    model = create_model('X_987 = ISOGONAL CONJUGATE OF X_986')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00987(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00987.json"))
    write_center_svg(
        model_acute,
        here / "x-00987.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
