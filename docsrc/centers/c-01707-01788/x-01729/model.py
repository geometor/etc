"""GEOMETOR construction model for X_1729 = MIMOSA TRANSFORM OF X_85."""

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
    incenter_of,
    mittenpunkt_of,
    nine_point_center_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01729(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1729 = MIMOSA TRANSFORM OF X_85 on reference triangle ABC."""
    X_331 = eval_trilinear_point(model, A, B, C, '(sec(A/2))**(2)*csc(2*A)', ID="X_331", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1729 = ceva_conjugate(model, A, B, C, X_331, X_1, ID="X_1729", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    central_line(model, X_5, X_9, 5, 9, incident=True)
    X_63 = eval_trilinear_point(model, A, B, C, 'cot(A)', ID="X_63", classes=["center", "incident"])
    X_169 = eval_trilinear_point(model, A, B, C, '- (sin(A))*(cos(A/2))**(2) + (sin(B))*(cos(B/2))**(2) + (sin(C))*(cos(C/2))**(2)', ID="X_169", classes=["center", "incident"])
    central_line(model, X_63, X_169, 63, 169, incident=True)
    X_19 = eval_trilinear_point(model, A, B, C, 'tan(A)', ID="X_19", classes=["center", "incident"])
    X_1158 = eval_trilinear_point(model, A, B, C, 'a**(6) - b**(6) - c**(6) + b**(2)*c**(2)*(b**(2) + c**(2)) + 3*a**(2)*(b**(4) + c**(4) - a**(2)*b**(2) - a**(2)*c**(2)) + 2*a*b*c*(a**(3) - b**(3) - c**(3) - a*b*c + (a**(2) + b*c)*(b + c) - a*b**(2) - a*c**(2))', ID="X_1158", classes=["center", "incident"])
    central_line(model, X_19, X_1158, 19, 1158, incident=True)
    return promote_point_to_top(model, X_1729)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1729 on the given reference triangle."""
    model = create_model('X_1729 = MIMOSA TRANSFORM OF X_85')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01729(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01729.json"))
    write_center_svg(
        model_acute,
        here / "x-01729.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
