"""GEOMETOR construction model for X_2351 = X_2-ISOCONJUGATE OF X_1748."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02351(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2351 = X_2-ISOCONJUGATE OF X_1748 on reference triangle ABC."""
    X_317 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)*(csc(A))**(2)', ID="X_317", classes=["center"])
    X_2351 = isogonal_conjugate(model, A, B, C, X_317, ID="X_2351", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X_68", classes=["center", "incident"])
    central_line(model, X_3, X_68, 3, 68, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    central_line(model, X_25, X_53, 25, 53, incident=True)
    X_32 = eval_trilinear_point(model, A, B, C, 'a**(3)', ID="X_32", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_32, X_51, 32, 51, incident=True)
    return promote_point_to_top(model, X_2351)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2351 on the given reference triangle."""
    model = create_model('X_2351 = X_2-ISOCONJUGATE OF X_1748')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02351(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02351.json"))
    write_center_svg(
        model_acute,
        here / "x-02351.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
