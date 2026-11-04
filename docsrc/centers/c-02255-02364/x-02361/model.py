"""GEOMETOR construction model for X_2361 = X_2-ISOCONJUGATE OF X_2006."""

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
    feuerbach_point_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02361(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2361 = X_2-ISOCONJUGATE OF X_2006 on reference triangle ABC."""
    X_2361 = eval_trilinear_point(model, A, B, C, 'cos(A/2)*cos(3*A/2)', ID="X_2361", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_31 = eval_trilinear_point(model, A, B, C, 'a**(2)', ID="X_31", classes=["center", "incident"])
    central_line(model, X_6, X_31, 6, 31, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_47 = eval_trilinear_point(model, A, B, C, 'cos(2*A)', ID="X_47", classes=["center", "incident"])
    central_line(model, X_3, X_47, 3, 47, incident=True)
    X_11 = feuerbach_point_of(model, A, B, C, ID="X_11", classes=["center", "incident"])
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    central_line(model, X_11, X_238, 11, 238, incident=True)
    return promote_point_to_top(model, X_2361)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2361 on the given reference triangle."""
    model = create_model('X_2361 = X_2-ISOCONJUGATE OF X_2006')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02361(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02361.json"))
    write_center_svg(
        model_acute,
        here / "x-02361.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
