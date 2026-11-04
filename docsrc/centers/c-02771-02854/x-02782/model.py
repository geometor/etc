"""GEOMETOR construction model for X_2782 = ISOGONAL CONJUGATE OF X_2698."""

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
    nine_point_center_of,
    orthocenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02782(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2782 = ISOGONAL CONJUGATE OF X_2698 on reference triangle ABC."""
    X_2698 = point_from_barycentrics(model, A, B, C, 0.78298709, -0.27279144, 0.48980435, ID="X_2698", classes=["center"])
    X_2782 = isogonal_conjugate(model, A, B, C, X_2698, ID="X_2782", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_39 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2))', ID="X_39", classes=["center", "incident"])
    central_line(model, X_5, X_39, 5, 39, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    central_line(model, X_3, X_76, 3, 76, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_147 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(8) + (b**(2) + c**(2))*a**(6) - (2*b**(4) + 3*b**(2)*c**(2) + 2*c**(4))*a**(4) + (b**(6) + b**(4)*c**(2) + b**(2)*c**(4) + c**(6))*a**(2) - b**(8) + b**(6)*c**(2) + b**(2)*c**(6) - c**(8))', ID="X_147", classes=["center", "incident"])
    central_line(model, X_4, X_147, 4, 147, incident=True)
    return promote_point_to_top(model, X_2782)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2782 on the given reference triangle."""
    model = create_model('X_2782 = ISOGONAL CONJUGATE OF X_2698')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02782(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02782.json"))
    write_center_svg(
        model_acute,
        here / "x-02782.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
