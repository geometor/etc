"""GEOMETOR construction model for X(570) = ORTHOGONAL OF X(52)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    circumcenter_of,
    complement,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00570(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(570) = ORTHOGONAL OF X(52) on reference triangle ABC."""
    X_311 = eval_barycentric_point(model, A, B, C, 'csc(A)*cos(B - C)', ID="X(311)", classes=["center"])
    X_570 = complement(model, A, B, C, X_311, ID="X(570)", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X(3)", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    X_128 = point_from_barycentrics(model, A, B, C, 0.43052912, -0.045594157, 0.61506504, ID="X(128)", classes=["center", "incident"])
    central_line(model, X_115, X_128, 115, 128, incident=True)
    X_53 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(B - C)', ID="X(53)", classes=["center", "incident"])
    X_232 = eval_trilinear_point(model, A, B, C, 'tan(A)*cos(A + omega )', ID="X(232)", classes=["center", "incident"])
    central_line(model, X_53, X_232, 53, 232, incident=True)
    return promote_point_to_top(model, X_570)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(570) on the given reference triangle."""
    model = create_model('X(570) = ORTHOGONAL OF X(52)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00570(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00570.json"))
    write_center_svg(
        model_acute,
        here / "x-00570.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
