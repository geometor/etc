"""GEOMETOR construction model for X_2287 = X_2-ISOCONJUGATE OF X_1042."""

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
    isogonal_conjugate,
    mittenpunkt_of,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02287(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2287 = X_2-ISOCONJUGATE OF X_1042 on reference triangle ABC."""
    X_1427 = point_from_barycentrics(model, A, B, C, 0.12974052, 0.25548902, 0.61477046, ID="X_1427", classes=["center"])
    X_2287 = isogonal_conjugate(model, A, B, C, X_1427, ID="X_2287", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_2, X_6, 2, 6, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_21 = eval_trilinear_point(model, A, B, C, '1/(cos(B) + cos(C))', ID="X_21", classes=["center", "incident"])
    central_line(model, X_9, X_21, 9, 21, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_29 = eval_trilinear_point(model, A, B, C, '(sec(A))/(cos(B) + cos(C))', ID="X_29", classes=["center", "incident"])
    central_line(model, X_8, X_29, 8, 29, incident=True)
    return promote_point_to_top(model, X_2287)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2287 on the given reference triangle."""
    model = create_model('X_2287 = X_2-ISOCONJUGATE OF X_1042')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02287(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02287.json"))
    write_center_svg(
        model_acute,
        here / "x-02287.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
