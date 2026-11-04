"""GEOMETOR construction model for X_1419 = X_144-BETH CONJUGATE OF X_144."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    mittenpunkt_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01419(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1419 = X_144-BETH CONJUGATE OF X_144 on reference triangle ABC."""
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_57 = eval_trilinear_point(model, A, B, C, '1/(b + c - a)', ID="X_57", classes=["center"])
    X_1419 = ceva_conjugate(model, A, B, C, X_1, X_57, ID="X_1419", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_6, X_57, 6, 57, incident=True)
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_77 = eval_trilinear_point(model, A, B, C, '1/(1 + sec(A))', ID="X_77", classes=["center", "incident"])
    central_line(model, X_9, X_77, 9, 77, incident=True)
    X_41 = eval_trilinear_point(model, A, B, C, 'a**(2)*(b + c - a)', ID="X_41", classes=["center", "incident"])
    X_738 = eval_trilinear_point(model, A, B, C, '((b + c - a) **(-3))', ID="X_738", classes=["center", "incident"])
    central_line(model, X_41, X_738, 41, 738, incident=True)
    return promote_point_to_top(model, X_1419)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1419 on the given reference triangle."""
    model = create_model('X_1419 = X_144-BETH CONJUGATE OF X_144')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01419(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01419.json"))
    write_center_svg(
        model_acute,
        here / "x-01419.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
