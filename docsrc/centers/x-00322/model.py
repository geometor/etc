"""GEOMETOR construction model for X(322) = ISOTOMIC CONJUGATE OF X(84)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    isotomic_conjugate,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00322(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(322) = ISOTOMIC CONJUGATE OF X(84) on reference triangle ABC."""
    X_84 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C) - cos(A) - 1)', ID="X(84)", classes=["center"])
    X_322 = isotomic_conjugate(model, A, B, C, X_84, ID="X(322)", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X(8)", classes=["center", "incident"])
    central_line(model, X_7, X_8, 7, 8, incident=True)
    X_78 = eval_trilinear_point(model, A, B, C, '1/(1 - sec(A))', ID="X(78)", classes=["center", "incident"])
    X_273 = eval_trilinear_point(model, A, B, C, 'sec(A)*(sec(A/2))**(2)', ID="X(273)", classes=["center", "incident"])
    central_line(model, X_78, X_273, 78, 273, incident=True)
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X(92)", classes=["center", "incident"])
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X(264)", classes=["center", "incident"])
    central_line(model, X_92, X_264, 92, 264, incident=True)
    return promote_point_to_top(model, X_322)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(322) on the given reference triangle."""
    model = create_model('X(322) = ISOTOMIC CONJUGATE OF X(84)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00322(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00322.json"))
    write_center_svg(
        model_acute,
        here / "x-00322.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
