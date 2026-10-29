"""GEOMETOR construction model for X(801) = ISOGONAL CONJUGATE OF X(800)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00801(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(801) = ISOGONAL CONJUGATE OF X(800) on reference triangle ABC."""
    X_800 = eval_barycentric_point(model, A, B, C, 'a**(2)*(a**(4)*(b**(2) + c**(2)) - 2*a**(2)*(b**(2) - c**(2))**(2) + (b**(2) - c**(2))**(2)*(b**(2) + c**(2)))', ID="X(800)", classes=["center"])
    X_801 = isogonal_conjugate(model, A, B, C, X_800, ID="X(801)", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X(10)", classes=["center", "incident"])
    X_775 = point_from_barycentrics(model, A, B, C, 0.43250342, 0.31571467, 0.25178191, ID="X(775)", classes=["center", "incident"])
    central_line(model, X_10, X_775, 10, 775, incident=True)
    return promote_point_to_top(model, X_801)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(801) on the given reference triangle."""
    model = create_model('X(801) = ISOGONAL CONJUGATE OF X(800)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00801(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00801.json"))
    write_center_svg(
        model_acute,
        here / "x-00801.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
