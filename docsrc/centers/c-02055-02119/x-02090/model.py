"""GEOMETOR construction model for X_2090 = 1st STEVANOVIC PERSPECTOR."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    nagel_point_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02090(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2090 = 1st STEVANOVIC PERSPECTOR on reference triangle ABC."""
    X_174 = eval_trilinear_point(model, A, B, C, 'sec(A/2)', ID="X_174", classes=["center"])
    X_2090 = complement(model, A, B, C, X_174, ID="X_2090", classes=["selected", "target"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_2, X_174, 2, 174, incident=True)
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    X_188 = eval_trilinear_point(model, A, B, C, 'csc(A/2)', ID="X_188", classes=["center", "incident"])
    central_line(model, X_8, X_188, 8, 188, incident=True)
    X_177 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*sec(A/2)', ID="X_177", classes=["center", "incident"])
    X_178 = eval_trilinear_point(model, A, B, C, '(cos(B/2) + cos(C/2))*csc(A)', ID="X_178", classes=["center", "incident"])
    central_line(model, X_177, X_178, 177, 178, incident=True)
    return promote_point_to_top(model, X_2090)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2090 on the given reference triangle."""
    model = create_model('X_2090 = 1st STEVANOVIC PERSPECTOR')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02090(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02090.json"))
    write_center_svg(
        model_acute,
        here / "x-02090.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
