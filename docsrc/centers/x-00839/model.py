"""GEOMETOR construction model for X(839) = o-(3, 4) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00839(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(839) = o-(3, 4) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_838 = point_from_barycentrics(model, A, B, C, -0.26139721, 0.80058936, -0.53919215, ID="X(838)", classes=["center"])
    X_839 = isogonal_conjugate(model, A, B, C, X_838, ID="X(839)", classes=["selected", "target"])
    X_110 = eval_trilinear_point(model, A, B, C, 'csc(B - C)', ID="X(110)", classes=["center", "incident"])
    X_668 = eval_trilinear_point(model, A, B, C, '1/(a**(2)*(b - c))', ID="X(668)", classes=["center", "incident"])
    central_line(model, X_110, X_668, 110, 668, incident=True)
    X_334 = eval_trilinear_point(model, A, B, C, 'b**(2)*c**(2)/(a**(2) - b*c)', ID="X(334)", classes=["center", "incident"])
    X_741 = point_from_barycentrics(model, A, B, C, -0.036241685, 0.96112949, 0.075112193, ID="X(741)", classes=["center", "incident"])
    central_line(model, X_334, X_741, 334, 741, incident=True)
    return promote_point_to_top(model, X_839)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(839) on the given reference triangle."""
    model = create_model('X(839) = o-(3, 4) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00839(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00839.json"))
    write_center_svg(
        model_acute,
        here / "x-00839.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
