"""GEOMETOR construction model for X_1019 = X_99-CEVA CONJUGATE OF X_1."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01019(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1019 = X_99-CEVA CONJUGATE OF X_1 on reference triangle ABC."""
    X_1018 = eval_trilinear_point(model, A, B, C, '((b + c)/(b - c))', ID="X_1018", classes=["center"])
    X_1019 = isogonal_conjugate(model, A, B, C, X_1018, ID="X_1019", classes=["selected", "target"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_36, X_238, 36, 238, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    central_line(model, X_1, X_512, 1, 512, incident=True)
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    X_514 = eval_trilinear_point(model, A, B, C, '(b - c)/a', ID="X_514", classes=["center", "incident"])
    central_line(model, X_239, X_514, 239, 514, incident=True)
    return promote_point_to_top(model, X_1019)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1019 on the given reference triangle."""
    model = create_model('X_1019 = X_99-CEVA CONJUGATE OF X_1')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01019(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01019.json"))
    write_center_svg(
        model_acute,
        here / "x-01019.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
