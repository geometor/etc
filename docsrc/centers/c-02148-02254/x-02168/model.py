"""GEOMETOR construction model for X_2168 = X_2-ISOCONJUGATE OF X_52."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02168(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2168 = X_2-ISOCONJUGATE OF X_52 on reference triangle ABC."""
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center"])
    X_1820 = eval_trilinear_point(model, A, B, C, 'tan(2*A)', ID="X_1820", classes=["center"])
    X_2168 = cevapoint(model, A, B, C, X_48, X_1820, ID="X_2168", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X_96", classes=["center", "incident"])
    central_line(model, X_10, X_96, 10, 96, incident=True)
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center", "incident"])
    central_line(model, X_48, X_91, 48, 91, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_563 = eval_trilinear_point(model, A, B, C, 'sin(4*A)', ID="X_563", classes=["center", "incident"])
    central_line(model, X_1, X_563, 1, 563, incident=True)
    return promote_point_to_top(model, X_2168)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2168 on the given reference triangle."""
    model = create_model('X_2168 = X_2-ISOCONJUGATE OF X_52')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02168(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02168.json"))
    write_center_svg(
        model_acute,
        here / "x-02168.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
