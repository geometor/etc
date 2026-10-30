"""GEOMETOR construction model for X(823) = ISOGONAL CONJUGATE OF X(822)."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00823(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(823) = ISOGONAL CONJUGATE OF X(822) on reference triangle ABC."""
    X_822 = eval_trilinear_point(model, A, B, C, 'csc(B/2) - csc(C/2)', ID="X(822)", classes=["center"])
    X_823 = isogonal_conjugate(model, A, B, C, X_822, ID="X(823)", classes=["selected", "target"])
    X_100 = eval_trilinear_point(model, A, B, C, '1/(b - c)', ID="X(100)", classes=["center", "incident"])
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X(107)", classes=["center", "incident"])
    central_line(model, X_100, X_107, 100, 107, incident=True)
    X_264 = eval_trilinear_point(model, A, B, C, 'csc(A)*csc(2*A)', ID="X(264)", classes=["center", "incident"])
    X_379 = point_from_barycentrics(model, A, B, C, 0.23688101, 0.27346637, 0.48965262, ID="X(379)", classes=["center", "incident"])
    central_line(model, X_264, X_379, 264, 379, incident=True)
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_681 = point_from_barycentrics(model, A, B, C, 0.48877447, -0.32158388, 0.83280941, ID="X(681)", classes=["center", "incident"])
    central_line(model, X_110, X_681, 110, 681, incident=True)
    return promote_point_to_top(model, X_823)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(823) on the given reference triangle."""
    model = create_model('X(823) = ISOGONAL CONJUGATE OF X(822)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00823(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00823.json"))
    write_center_svg(
        model_acute,
        here / "x-00823.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
