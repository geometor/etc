"""GEOMETOR construction model for X(987) = ISOGONAL CONJUGATE OF X(986)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00987(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(987) = ISOGONAL CONJUGATE OF X(986) on reference triangle ABC."""
    X_986 = point_from_barycentrics(model, A, B, C, 0.30540209, 0.34438306, 0.35021486, ID="X(986)", classes=["center"])
    X_987 = isogonal_conjugate(model, A, B, C, X_986, ID="X(987)", classes=["selected", "target"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X(31)", classes=["center", "incident"])
    central_line(model, X_8, X_31, 8, 31, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X(32)", classes=["center", "incident"])
    central_line(model, X_9, X_32, 9, 32, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_171 = eval_trilinear_point(model, A, B, C, 'a**(2) + b*c', ID="X(171)", classes=["center", "incident"])
    central_line(model, X_4, X_171, 4, 171, incident=True)
    return promote_point_to_top(model, X_987)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(987) on the given reference triangle."""
    model = create_model('X(987) = ISOGONAL CONJUGATE OF X(986)')
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
