"""GEOMETOR construction model for X_3618 = H(X_6; M,1/2)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_03618(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3618 = H(X_6; M,1/2) on reference triangle ABC."""
    X_3618 = eval_trilinear_point(model, A, B, C, '(b*c*(3*a**(2) + b**(2) + c**(2)))', ID="X_3618", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_83 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) + c**(2))', ID="X_83", classes=["center", "incident"])
    central_line(model, X_4, X_83, 4, 83, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_344 = eval_trilinear_point(model, A, B, C, '((csc(A/2))**(2))*((cos(B/2))**(4) + (cos(C/2))**(4) - (cos(A/2))**(4))', ID="X_344", classes=["center", "incident"])
    central_line(model, X_1, X_344, 1, 344, incident=True)
    return promote_point_to_top(model, X_3618)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3618 on the given reference triangle."""
    model = create_model('X_3618 = H(X_6; M,1/2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03618(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03618.json"))
    write_center_svg(
        model_acute,
        here / "x-03618.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
