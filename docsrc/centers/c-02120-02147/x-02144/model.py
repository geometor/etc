"""GEOMETOR construction model for X_2144 = X_2-EIGENTRANSFORM OF X_238."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02144(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2144 = X_2-EIGENTRANSFORM OF X_238 on reference triangle ABC."""
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center"])
    X_292 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) - b*c)', ID="X_292", classes=["center"])
    X_2144 = ceva_conjugate(model, A, B, C, X_238, X_292, ID="X_2144", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2111 = eval_trilinear_point(model, A, B, C, '(1/((b**(2) + b*c + c**(2))*a**(3) - (b + c)*(b**(2) + c**(2))*a**(2) - b*c*(b**(2) - b*c + c**(2))*a + b**(2)*c**(2)*(b + c)))', ID="X_2111", classes=["center", "incident"])
    central_line(model, X_1, X_2111, 1, 2111, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_2113 = eval_trilinear_point(model, A, B, C, '(1/(a**(4) - b*c*a**(2) - (b**(3) + c**(3))*a + 2*b**(2)*c**(2)))', ID="X_2113", classes=["center", "incident"])
    central_line(model, X_2, X_2113, 2, 2113, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_2109 = eval_trilinear_point(model, A, B, C, '(a/((b + c)*a**(3) - (b**(2) - b*c + c**(2))*a**(2) - (b + c)*(b**(2) + c**(2))*a + b*c*(b**(2) + b*c + c**(2))))', ID="X_2109", classes=["center", "incident"])
    central_line(model, X_6, X_2109, 6, 2109, incident=True)
    return promote_point_to_top(model, X_2144)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2144 on the given reference triangle."""
    model = create_model('X_2144 = X_2-EIGENTRANSFORM OF X_238')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02144(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02144.json"))
    write_center_svg(
        model_acute,
        here / "x-02144.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
