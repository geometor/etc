"""GEOMETOR construction model for X(673) = TRILINEAR POLE OF LINE X(1)X(514)."""

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
    feuerbach_point_of,
    gergonne_point_of,
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00673(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(673) = TRILINEAR POLE OF LINE X(1)X(514) on reference triangle ABC."""
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X(672)", classes=["center"])
    X_673 = isogonal_conjugate(model, A, B, C, X_672, ID="X(673)", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_11 = feuerbach_point_of(model, A, B, C, ID="X(11)", classes=["center", "incident"])
    central_line(model, X_2, X_11, 2, 11, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X(7)", classes=["center", "incident"])
    central_line(model, X_6, X_7, 6, 7, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X(9)", classes=["center", "incident"])
    X_75 = eval_trilinear_point(model, A, B, C, '1/a**(2)', ID="X(75)", classes=["center", "incident"])
    central_line(model, X_9, X_75, 9, 75, incident=True)
    return promote_point_to_top(model, X_673)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(673) on the given reference triangle."""
    model = create_model('X(673) = TRILINEAR POLE OF LINE X(1)X(514)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00673(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00673.json"))
    write_center_svg(
        model_acute,
        here / "x-00673.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
