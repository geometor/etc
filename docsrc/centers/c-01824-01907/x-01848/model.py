"""GEOMETOR construction model for X_1848 = ZOSMA TRANSFORM OF X_171."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    incenter_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01848(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1848 = ZOSMA TRANSFORM OF X_171 on reference triangle ABC."""
    X_27 = eval_trilinear_point(model, A, B, C, '(sec(A))/(b + c)', ID="X_27", classes=["center"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center"])
    X_1848 = crosspoint(model, A, B, C, X_27, X_92, ID="X_1848", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    central_line(model, X_1, X_4, 1, 4, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    central_line(model, X_2, X_19, 2, 19, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X_86", classes=["center", "incident"])
    central_line(model, X_27, X_86, 27, 86, incident=True)
    return promote_point_to_top(model, X_1848)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1848 on the given reference triangle."""
    model = create_model('X_1848 = ZOSMA TRANSFORM OF X_171')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01848(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01848.json"))
    write_center_svg(
        model_acute,
        here / "x-01848.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
