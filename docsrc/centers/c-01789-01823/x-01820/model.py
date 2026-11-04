"""GEOMETOR construction model for X_1820 = ISOGONAL CONJUGATE OF MIMOSA TRANSFORM OF X_264."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01820(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1820 = ISOGONAL CONJUGATE OF MIMOSA TRANSFORM OF X_264 on reference triangle ABC."""
    X_1748 = eval_trilinear_point(model, A, B, C, 'cot(A) - tan(A)', ID="X_1748", classes=["center"])
    X_1820 = isogonal_conjugate(model, A, B, C, X_1748, ID="X_1820", classes=["selected", "target"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_91 = eval_trilinear_point(model, A, B, C, 'sec(2*A)', ID="X_91", classes=["center", "incident"])
    central_line(model, X_19, X_91, 19, 91, incident=True)
    X_68 = eval_trilinear_point(model, A, B, C, 'cos(A)*sec(2*A)', ID="X_68", classes=["center", "incident"])
    X_71 = eval_trilinear_point(model, A, B, C, '(b + c)*cos(A)', ID="X_71", classes=["center", "incident"])
    central_line(model, X_68, X_71, 68, 71, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_563 = eval_trilinear_point(model, A, B, C, 'sin(4*A)', ID="X_563", classes=["center", "incident"])
    central_line(model, X_1, X_563, 1, 563, incident=True)
    return promote_point_to_top(model, X_1820)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1820 on the given reference triangle."""
    model = create_model('X_1820 = ISOGONAL CONJUGATE OF MIMOSA TRANSFORM OF X_264')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01820(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01820.json"))
    write_center_svg(
        model_acute,
        here / "x-01820.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
