"""GEOMETOR construction model for X_1609 = TCC-PERSPECTOR OF X_19."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    construct_baseline_triangle,
    create_model,
    crosspoint,
    eval_trilinear_point,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_01609(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1609 = TCC-PERSPECTOR OF X_19 on reference triangle ABC."""
    X_107 = eval_trilinear_point(model, A, B, C, '1/(cos(A)*(sin(2*B) - sin(2*C)))', ID="X_107", classes=["center"])
    X_249 = eval_trilinear_point(model, A, B, C, '(csc(A))*(csc(B - C))**(2)', ID="X_249", classes=["center"])
    X_1609 = crosspoint(model, A, B, C, X_107, X_249, ID="X_1609", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X_53", classes=["center", "incident"])
    central_line(model, X_25, X_53, 25, 53, incident=True)
    X_24 = eval_trilinear_point(model, A, B, C, 'sec(A)*cos(2*A)', ID="X_24", classes=["center", "incident"])
    X_254 = eval_trilinear_point(model, A, B, C, '(sec(A))/((cos(B))**(2) + (cos(C))**(2) - (cos(A))**(2))', ID="X_254", classes=["center", "incident"])
    central_line(model, X_24, X_254, 24, 254, incident=True)
    return promote_point_to_top(model, X_1609)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1609 on the given reference triangle."""
    model = create_model('X_1609 = TCC-PERSPECTOR OF X_19')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01609(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01609.json"))
    write_center_svg(
        model_acute,
        here / "x-01609.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
