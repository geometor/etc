"""GEOMETOR construction model for X_2731 = SR(X_102, X_106)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    intersect_lines,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02731(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2731 = SR(X_102, X_106) on reference triangle ABC."""
    X_102 = eval_trilinear_point(model, A, B, C, '1/(sin(B)*(sec(A) - sec(B)) + sin(C)*(sec(A) - sec(C)))', ID="X_102", classes=["center"])
    X_519 = eval_trilinear_point(model, A, B, C, '(2*a - b - c)/a', ID="X_519", classes=["center"])
    X_106 = eval_trilinear_point(model, A, B, C, 'a/(2*a - b - c)', ID="X_106", classes=["center"])
    X_515 = eval_trilinear_point(model, A, B, C, '(b + c)*sec(A) - b*sec(B) - c*sec(C)', ID="X_515", classes=["center"])
    central_line(model, X_102, X_519, 102, 519)
    central_line(model, X_106, X_515, 106, 515)
    X_2731 = intersect_lines(model, X_102, X_519, X_106, X_515, ID="X_2731", classes=["selected", "target"])
    X_522 = eval_trilinear_point(model, A, B, C, '(cos(B) - cos(C))*(csc(A))', ID="X_522", classes=["center", "incident"])
    X_1293 = eval_trilinear_point(model, A, B, C, '(a/((b - c)*(3*a - b - c)))', ID="X_1293", classes=["center", "incident"])
    central_line(model, X_522, X_1293, 522, 1293, incident=True)
    return promote_point_to_top(model, X_2731)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2731 on the given reference triangle."""
    model = create_model('X_2731 = SR(X_102, X_106)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02731(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02731.json"))
    write_center_svg(
        model_acute,
        here / "x-02731.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
