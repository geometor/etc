"""GEOMETOR construction model for X(873) = ISOGONAL CONJUGATE OF X(872)."""

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
    isogonal_conjugate,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00873(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(873) = ISOGONAL CONJUGATE OF X(872) on reference triangle ABC."""
    X_872 = eval_trilinear_point(model, A, B, C, '(a*(b + c))**(2)', ID="X(872)", classes=["center"])
    X_873 = isogonal_conjugate(model, A, B, C, X_872, ID="X(873)", classes=["selected", "target"])
    X_81 = eval_trilinear_point(model, A, B, C, '1/(b + c)', ID="X(81)", classes=["center", "incident"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X(239)", classes=["center", "incident"])
    central_line(model, X_81, X_239, 81, 239, incident=True)
    X_86 = eval_trilinear_point(model, A, B, C, 'b*c/(b + c)', ID="X(86)", classes=["center", "incident"])
    X_310 = eval_trilinear_point(model, A, B, C, 'b**(3)*c**(3)/(b + c)', ID="X(310)", classes=["center", "incident"])
    central_line(model, X_86, X_310, 86, 310, incident=True)
    X_2 = centroid_of(model, A, B, C, ID="X(2)", classes=["center", "incident"])
    X_799 = eval_barycentric_point(model, A, B, C, 'b*c/(b**(2) - c**(2))', ID="X(799)", classes=["center", "incident"])
    central_line(model, X_2, X_799, 2, 799, incident=True)
    return promote_point_to_top(model, X_873)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(873) on the given reference triangle."""
    model = create_model('X(873) = ISOGONAL CONJUGATE OF X(872)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00873(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00873.json"))
    write_center_svg(
        model_acute,
        here / "x-00873.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
