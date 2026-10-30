"""GEOMETOR construction model for X(327) = ISOTOMIC CONJUGATE OF X(182)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isotomic_conjugate,
    nine_point_center_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00327(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(327) = ISOTOMIC CONJUGATE OF X(182) on reference triangle ABC."""
    X_182 = eval_trilinear_point(model, A, B, C, 'cos(A- omega )', ID="X(182)", classes=["center"])
    X_327 = isotomic_conjugate(model, A, B, C, X_182, ID="X(327)", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X(5)", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    central_line(model, X_5, X_76, 5, 76, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center", "incident"])
    X_141 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) + c**(2))', ID="X(141)", classes=["center", "incident"])
    central_line(model, X_53, X_141, 53, 141, incident=True)
    X_95 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)*sec(B - C)', ID="X(95)", classes=["center", "incident"])
    X_160 = point_from_barycentrics(model, A, B, C, 0.55772762, 0.55017141, -0.10789903, ID="X(160)", classes=["center", "incident"])
    central_line(model, X_95, X_160, 95, 160, incident=True)
    return promote_point_to_top(model, X_327)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(327) on the given reference triangle."""
    model = create_model('X(327) = ISOTOMIC CONJUGATE OF X(182)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00327(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00327.json"))
    write_center_svg(
        model_acute,
        here / "x-00327.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
