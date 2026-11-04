"""GEOMETOR construction model for X_1463 = X_726-BETH CONJUGATE OF X_726."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    ceva_conjugate,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    gergonne_point_of,
    nagel_point_of,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01463(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1463 = X_726-BETH CONJUGATE OF X_726 on reference triangle ABC."""
    X_1447 = point_from_barycentrics(model, A, B, C, -0.76119403, 0.059701493, 1.7014925, ID="X_1447", classes=["center"])
    X_241 = eval_trilinear_point(model, A, B, C, '(cos(B/2))**(4) - ((cos(A/2))**(2))*((cos(B/2))**(2) +(cos(C/2))**(2)) + (cos(C/2))**(4)', ID="X_241", classes=["center"])
    X_1463 = ceva_conjugate(model, A, B, C, X_1447, X_241, ID="X_1463", classes=["selected", "target"])
    X_7 = gergonne_point_of(model, A, B, C, ID="X_7", classes=["center", "incident"])
    X_8 = nagel_point_of(model, A, B, C, ID="X_8", classes=["center", "incident"])
    central_line(model, X_7, X_8, 7, 8, incident=True)
    X_56 = eval_trilinear_point(model, A, B, C, 'a/(b + c - a)', ID="X_56", classes=["center", "incident"])
    X_87 = eval_trilinear_point(model, A, B, C, '1/(a*b + a*c - b*c)', ID="X_87", classes=["center", "incident"])
    central_line(model, X_56, X_87, 56, 87, incident=True)
    X_44 = eval_trilinear_point(model, A, B, C, 'b + c - 2*a', ID="X_44", classes=["center", "incident"])
    X_583 = eval_trilinear_point(model, A, B, C, '(a*(a**(2)*b + a**(2)*c + 2*a*b*c - b**(3) - c**(3)))', ID="X_583", classes=["center", "incident"])
    central_line(model, X_44, X_583, 44, 583, incident=True)
    return promote_point_to_top(model, X_1463)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1463 on the given reference triangle."""
    model = create_model('X_1463 = X_726-BETH CONJUGATE OF X_726')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01463(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01463.json"))
    write_center_svg(
        model_acute,
        here / "x-01463.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
