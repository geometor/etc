"""GEOMETOR construction model for X_2921 = TANGENTIAL-ISOGONAL CONJUGATE OF X_9."""

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
    intersect_lines,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02921(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2921 = TANGENTIAL-ISOGONAL CONJUGATE OF X_9 on reference triangle ABC."""
    X_22 = eval_trilinear_point(model, A, B, C, 'a*(b**(4) + c**(4) - a**(4))', ID="X_22", classes=["center"])
    X_347 = eval_trilinear_point(model, A, B, C, '((-1 - cos(A) + cos(B) + cos(C))*(sec(A/2))**(2))', ID="X_347", classes=["center"])
    X_36 = eval_trilinear_point(model, A, B, C, '1 - 2*cos(A)', ID="X_36", classes=["center"])
    X_1104 = point_from_barycentrics(model, A, B, C, 0.17229255, 0.32067511, 0.50703235, ID="X_1104", classes=["center"])
    central_line(model, X_22, X_347, 22, 347)
    central_line(model, X_36, X_1104, 36, 1104)
    X_2921 = intersect_lines(model, X_22, X_347, X_36, X_1104, ID="X_2921", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_1603 = point_from_barycentrics(model, A, B, C, 1.1738452, 1.1872659, -1.3611111, ID="X_1603", classes=["center", "incident"])
    central_line(model, X_3, X_1603, 3, 1603, incident=True)
    return promote_point_to_top(model, X_2921)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2921 on the given reference triangle."""
    model = create_model('X_2921 = TANGENTIAL-ISOGONAL CONJUGATE OF X_9')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02921(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02921.json"))
    write_center_svg(
        model_acute,
        here / "x-02921.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
