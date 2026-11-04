"""GEOMETOR construction model for X_2607 = CROSSDIFFERENCE OF PU(70)."""

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
    incenter_of,
    mittenpunkt_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02607(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2607 = CROSSDIFFERENCE OF PU(70) on reference triangle ABC."""
    X_2607 = eval_trilinear_point(model, A, B, C, 'sin(A - B)*sin(A - C) + (sin(B - C))**(2)', ID="X_2607", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    central_line(model, X_9, X_46, 9, 46, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_523 = eval_trilinear_point(model, A, B, C, 'sin(B -C)', ID="X_523", classes=["center", "incident"])
    central_line(model, X_1, X_523, 1, 523, incident=True)
    X_229 = point_from_barycentrics(model, A, B, C, 0.21061481, 0.29086323, 0.49852195, ID="X_229", classes=["center", "incident"])
    X_409 = eval_barycentric_point(model, A, B, C, 'a*(a + b) * (a + c) * (a**(4) - a**(3)*b + a*b**(3) - b**(4) - a**(3)*c + a**(2)*b*c + a*b**(2)*c + b**(3)*c + a*b*c**(2) + 4*b**(2)*c**(2) + a*c**(3) + b*c**(3) - c**(4))', ID="X_409", classes=["center", "incident"])
    central_line(model, X_229, X_409, 229, 409, incident=True)
    return promote_point_to_top(model, X_2607)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2607 on the given reference triangle."""
    model = create_model('X_2607 = CROSSDIFFERENCE OF PU(70)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02607(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02607.json"))
    write_center_svg(
        model_acute,
        here / "x-02607.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
