"""GEOMETOR construction model for X_2182 = X_2-ISOCONJUGATE OF X_102."""

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
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02182(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2182 = X_2-ISOCONJUGATE OF X_102 on reference triangle ABC."""
    X_2182 = eval_trilinear_point(model, A, B, C, 'a*((b + c)*sec(A) - b*sec(B) - c*sec(C))', ID="X_2182", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_3, X_9, 3, 9, incident=True)
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_6, X_19, 6, 19, incident=True)
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    central_line(model, X_37, X_48, 37, 48, incident=True)
    return promote_point_to_top(model, X_2182)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2182 on the given reference triangle."""
    model = create_model('X_2182 = X_2-ISOCONJUGATE OF X_102')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02182(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02182.json"))
    write_center_svg(
        model_acute,
        here / "x-02182.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
