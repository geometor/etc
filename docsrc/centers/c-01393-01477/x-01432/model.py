"""GEOMETOR construction model for X_1432 = X_257-BETH CONJUGATE OF X_257."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    cevapoint,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    incenter_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01432(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1432 = X_257-BETH CONJUGATE OF X_257 on reference triangle ABC."""
    X_893 = eval_trilinear_point(model, A, B, C, 'a/(a**(2) + b*c)', ID="X_893", classes=["center"])
    X_1431 = point_from_barycentrics(model, A, B, C, 0.16296232, 0.29526018, 0.54177751, ID="X_1431", classes=["center"])
    X_1432 = cevapoint(model, A, B, C, X_893, X_1431, ID="X_1432", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_256 = eval_trilinear_point(model, A, B, C, '1/(a**(2) + b*c)', ID="X_256", classes=["center", "incident"])
    central_line(model, X_1, X_256, 1, 256, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    X_257 = eval_trilinear_point(model, A, B, C, '1/(a**(3) + a*b*c)', ID="X_257", classes=["center", "incident"])
    central_line(model, X_2, X_257, 2, 257, incident=True)
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_330 = eval_trilinear_point(model, A, B, C, 'b*c/(a*b + a*c - b*c)', ID="X_330", classes=["center", "incident"])
    central_line(model, X_7, X_330, 7, 330, incident=True)
    return promote_point_to_top(model, X_1432)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1432 on the given reference triangle."""
    model = create_model('X_1432 = X_257-BETH CONJUGATE OF X_257')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01432(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01432.json"))
    write_center_svg(
        model_acute,
        here / "x-01432.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
