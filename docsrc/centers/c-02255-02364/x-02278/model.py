"""GEOMETOR construction model for X_2278 = X_2-ISOCONJUGATE OF X_994."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02278(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2278 = X_2-ISOCONJUGATE OF X_994 on reference triangle ABC."""
    X_2278 = eval_trilinear_point(model, A, B, C, '(sin(A) + sin(B) + sin(C))*cos(A) + (cos(A) + cos(B) + cos(C))*sin(A)', ID="X_2278", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_37, X_48, 37, 48, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    central_line(model, X_41, X_44, 41, 44, incident=True)
    return promote_point_to_top(model, X_2278)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2278 on the given reference triangle."""
    model = create_model('X_2278 = X_2-ISOCONJUGATE OF X_994')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02278(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02278.json"))
    write_center_svg(
        model_acute,
        here / "x-02278.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
