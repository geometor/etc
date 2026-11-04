"""GEOMETOR construction model for X_1436 = X_282-BETH CONJUGATE OF X_282."""

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
    isogonal_conjugate,
    mittenpunkt_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01436(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1436 = X_282-BETH CONJUGATE OF X_282 on reference triangle ABC."""
    X_329 = eval_trilinear_point(model, A, B, C, '( -1 - cos(A) + cos(B) + cos(C))*(csc(A))', ID="X_329", classes=["center"])
    X_1436 = isogonal_conjugate(model, A, B, C, X_329, ID="X_1436", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_3, X_9, 3, 9, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    central_line(model, X_19, X_56, 19, 56, incident=True)
    X_48 = eval_trilinear_point(model, A, B, C, 'tan(B) + tan(C)', ID="X_48", classes=["center", "incident"])
    X_55 = eval_trilinear_point(model, A, B, C, 'a*(b + c - a)', ID="X_55", classes=["center", "incident"])
    central_line(model, X_48, X_55, 48, 55, incident=True)
    return promote_point_to_top(model, X_1436)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1436 on the given reference triangle."""
    model = create_model('X_1436 = X_282-BETH CONJUGATE OF X_282')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01436(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01436.json"))
    write_center_svg(
        model_acute,
        here / "x-01436.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
