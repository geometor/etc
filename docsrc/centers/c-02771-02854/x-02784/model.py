"""GEOMETOR construction model for X_2784 = ISOGONAL CONJUGATE OF X_2700."""

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
    point_from_barycentrics,
    promote_point_to_top,
    spieker_center_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02784(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2784 = ISOGONAL CONJUGATE OF X_2700 on reference triangle ABC."""
    X_2700 = point_from_barycentrics(model, A, B, C, 0.90414101, -0.16964973, 0.26550872, ID="X_2700", classes=["center"])
    X_2784 = isogonal_conjugate(model, A, B, C, X_2700, ID="X_2784", classes=["selected", "target"])
    X_10 = spieker_center_of(model, A, B, C, ID="X_10", classes=["center", "incident"])
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    central_line(model, X_10, X_98, 10, 98, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_147 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(8) + (b**(2) + c**(2))*a**(6) - (2*b**(4) + 3*b**(2)*c**(2) + 2*c**(4))*a**(4) + (b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + c**(6))*a**(2) - b**(8) + b**(6)*c**(2) + b**(2)*c**(6) - c**(8))', ID="X_147", classes=["center", "incident"])
    central_line(model, X_1, X_147, 1, 147, incident=True)
    X_99 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X_99", classes=["center", "incident"])
    X_103 = eval_trilinear_point(model, A, B, C, 'a/((a - b)*cot(C) + (a - c)*cot(B))', ID="X_103", classes=["center", "incident"])
    central_line(model, X_99, X_103, 99, 103, incident=True)
    return promote_point_to_top(model, X_2784)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2784 on the given reference triangle."""
    model = create_model('X_2784 = ISOGONAL CONJUGATE OF X_2700')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02784(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02784.json"))
    write_center_svg(
        model_acute,
        here / "x-02784.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
