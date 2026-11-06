"""GEOMETOR construction model for X_3625 = H⁻¹(X_1; M, -1/2)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    centroid_of,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    incenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_03625(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_3625 = H⁻¹(X_1; M, -1/2) on reference triangle ABC."""
    X_3625 = eval_trilinear_point(model, A, B, C, 'b*c*(4*a - 3*b - 3*c)', ID="X_3625", classes=["selected", "target"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_2 = centroid_of(model, A, B, C, ID="X_2", classes=["center", "incident"])
    central_line(model, X_1, X_2, 1, 2, incident=True)
    X_548 = eval_trilinear_point(model, A, B, C, '- cos(B - C) + 6*cos(A)', ID="X_548", classes=["center", "incident"])
    X_952 = eval_trilinear_point(model, A, B, C, 'b*c*(2*a**(4) - 2*a**(3)*(b + c) - a**(2)*(b**(2) - 4*b*c + c**(2)) + (2*a - b - c)*(b - c)*(b**(2) - c**(2)))', ID="X_952", classes=["center", "incident"])
    central_line(model, X_548, X_952, 548, 952, incident=True)
    X_536 = eval_barycentric_point(model, A, B, C, '2*b*c - c*a - a*b', ID="X_536", classes=["center", "incident"])
    X_1358 = eval_trilinear_point(model, A, B, C, '(tan(A/2))**(2)*(sin(B/2 - C/2))**(2)', ID="X_1358", classes=["center", "incident"])
    central_line(model, X_536, X_1358, 536, 1358, incident=True)
    return promote_point_to_top(model, X_3625)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_3625 on the given reference triangle."""
    model = create_model('X_3625 = H⁻¹(X_1; M, -1/2)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_03625(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-03625.json"))
    write_center_svg(
        model_acute,
        here / "x-03625.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
