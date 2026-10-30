"""GEOMETOR construction model for X(761) = EVEN (1, 4) CIRCUMCIRCLE POINT."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    incenter_of,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00761(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(761) = EVEN (1, 4) CIRCUMCIRCLE POINT on reference triangle ABC."""
    X_760 = point_from_barycentrics(model, A, B, C, -0.61673691, -0.15501766, 0.77175457, ID="X(760)", classes=["center"])
    X_761 = isogonal_conjugate(model, A, B, C, X_760, ID="X(761)", classes=["selected", "target"])
    X_665 = eval_trilinear_point(model, A, B, C, 'a*((a - b)**(2)*(a + b - c) - (c - a)**(2)*(c + a - b))', ID="X(665)", classes=["center", "incident"])
    X_743 = point_from_barycentrics(model, A, B, C, -0.00071359148, 0.99931351, 0.001400079, ID="X(743)", classes=["center", "incident"])
    central_line(model, X_665, X_743, 665, 743, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X(1)", classes=["center", "incident"])
    X_825 = eval_trilinear_point(model, A, B, C, '1/(a**(-1)*(b**(3) - c**(3)) + a**(2)*(b**(0) - c**(0)))', ID="X(825)", classes=["center", "incident"])
    central_line(model, X_1, X_825, 1, 825, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X(76)", classes=["center", "incident"])
    X_789 = eval_trilinear_point(model, A, B, C, 'a **(- 2)/(b**(3) - c**(3))', ID="X(789)", classes=["center", "incident"])
    central_line(model, X_76, X_789, 76, 789, incident=True)
    return promote_point_to_top(model, X_761)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(761) on the given reference triangle."""
    model = create_model('X(761) = EVEN (1, 4) CIRCUMCIRCLE POINT')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00761(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00761.json"))
    write_center_svg(
        model_acute,
        here / "x-00761.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
