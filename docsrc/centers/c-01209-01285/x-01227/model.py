"""GEOMETOR construction model for X_1227 = ISOTOMIC CONJUGATE OF X_1168."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    isotomic_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01227(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1227 = ISOTOMIC CONJUGATE OF X_1168 on reference triangle ABC."""
    X_1168 = point_from_barycentrics(model, A, B, C, 4.7580987e-17, 1, 6.6613381e-17, ID="X_1168", classes=["center"])
    X_1227 = isotomic_conjugate(model, A, B, C, X_1168, ID="X_1227", classes=["selected", "target"])
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_190 = eval_trilinear_point(model, A, B, C, 'b*c/(b - c)', ID="X_190", classes=["center", "incident"])
    central_line(model, X_63, X_190, 63, 190, incident=True)
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X_75", classes=["center", "incident"])
    X_537 = point_from_barycentrics(model, A, B, C, 0.47409982, -0.81274255, 0.33864273, ID="X_537", classes=["center", "incident"])
    central_line(model, X_75, X_537, 75, 537, incident=True)
    X_321 = eval_trilinear_point(model, A, B, C, '(b + c)*b**(2)*c**(2)', ID="X_321", classes=["center", "incident"])
    X_545 = eval_barycentric_point(model, A, B, C, '2*a**(2) - b**(2) - c**(2) - 2*a*b - 2*a*c + 4*b*c', ID="X_545", classes=["center", "incident"])
    central_line(model, X_321, X_545, 321, 545, incident=True)
    return promote_point_to_top(model, X_1227)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1227 on the given reference triangle."""
    model = create_model('X_1227 = ISOTOMIC CONJUGATE OF X_1168')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01227(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01227.json"))
    write_center_svg(
        model_acute,
        here / "x-01227.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
