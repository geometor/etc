"""GEOMETOR construction model for X(503) = 1st ISOSCELIZER POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00503(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(503) = 1st ISOSCELIZER POINT on reference triangle ABC."""
    X_259 = eval_trilinear_point(model, A, B, C, 'cos(A/2)', ID="X(259)", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center"])
    X_503 = ceva_conjugate(model, A, B, C, X_259, X_1, ID="X(503)", classes=["selected", "target"])
    X_167 = point_from_barycentrics(model, A, B, C, 0.58849841, 0.49152493, -0.080023337, ID="X(167)", classes=["center", "incident"])
    central_line(model, X_1, X_167, 1, 167, incident=True)
    X_164 = eval_trilinear_point(model, A, B, C, 'sin(B/2) + sin(C/2) - sin(A/2)', ID="X(164)", classes=["center", "incident"])
    X_361 = eval_trilinear_point(model, A, B, C, 'csc(B/2) + csc(C/2) - csc(A/2)', ID="X(361)", classes=["center", "incident"])
    central_line(model, X_164, X_361, 164, 361, incident=True)
    X_173 = eval_trilinear_point(model, A, B, C, 'cos(B/2) + cos(C/2) - cos(A/2)', ID="X(173)", classes=["center", "incident"])
    X_844 = point_from_barycentrics(model, A, B, C, 0.53778809, 0.45817273, 0.0040391758, ID="X(844)", classes=["center", "incident"])
    central_line(model, X_173, X_844, 173, 844, incident=True)
    return promote_point_to_top(model, X_503)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(503) on the given reference triangle."""
    model = create_model('X(503) = 1st ISOSCELIZER POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00503(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00503.json"))
    write_center_svg(
        model_acute,
        here / "x-00503.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
