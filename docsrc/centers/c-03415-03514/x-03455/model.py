"""GEOMETOR construction model for X_3455 = X_13-VERTEX CONJUGATE OF X_14."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03455(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3455 = X_13-VERTEX CONJUGATE OF X_14 on reference triangle ABC."""
    X_316 = eval_trilinear_point(model, A, B, C, '(b*c*(b**(4) + c**(4) - a**(4) - b**(2)*c**(2)))', ID="X_316", classes=["center"])
    X_3455 = isogonal_conjugate(model, A, B, C, X_316, ID="X_3455", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_67 = eval_trilinear_point(model, A, B, C, 'b*c/(b**(4) + c**(4) - a**(4) - b**(2)*c**(2))', ID="X_67", classes=["center", "incident"])
    central_line(model, X_3, X_67, 3, 67, incident=True)
    X_25 = eval_trilinear_point(model, A, B, C, 'sin(A)*tan(A)', ID="X_25", classes=["center", "incident"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X_115", classes=["center", "incident"])
    central_line(model, X_25, X_115, 25, 115, incident=True)
    X_98 = eval_trilinear_point(model, A, B, C, 'sec(A +  omega  )', ID="X_98", classes=["center", "incident"])
    X_186 = eval_trilinear_point(model, A, B, C, '4*cos(A) - sec(A)', ID="X_186", classes=["center", "incident"])
    central_line(model, X_98, X_186, 98, 186, incident=True)
    return promote_point_to_top(model, X_3455)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3455 on the given reference triangle."""
    model = create_model('X_3455 = X_13-VERTEX CONJUGATE OF X_14')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03455(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03455.json"))
    write_center_svg(
        model_acute,
        here / "x-03455.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
