"""GEOMETOR construction model for X_1154 = ISOGONAL CONJUGATE OF X_1141."""

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
    nine_point_center_of,
    orthocenter_of,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01154(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1154 = ISOGONAL CONJUGATE OF X_1141 on reference triangle ABC."""
    X_1141 = eval_trilinear_point(model, A, B, C, 'b*c/(16*D**(2) + (a**(2)+c**(2)-b**(2))*(a**(2)+b**(2)-c**(2)))*(16*D**(2) - 3*(b**(2)+c**(2)-a**(2))**(2))', ID="X_1141", classes=["center"])
    X_1154 = isogonal_conjugate(model, A, B, C, X_1141, ID="X_1154", classes=["selected", "target"])
    X_5 = nine_point_center_of(model, A, B, C, ID="X_5", classes=["center", "incident"])
    X_51 = eval_trilinear_point(model, A, B, C, 'a**(2)*cos(B - C)', ID="X_51", classes=["center", "incident"])
    central_line(model, X_5, X_51, 5, 51, incident=True)
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_54 = eval_trilinear_point(model, A, B, C, 'sec(B - C)', ID="X_54", classes=["center", "incident"])
    central_line(model, X_3, X_54, 3, 54, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X_4", classes=["center", "incident"])
    X_93 = eval_trilinear_point(model, A, B, C, 'sec(3*A)', ID="X_93", classes=["center", "incident"])
    central_line(model, X_4, X_93, 4, 93, incident=True)
    return promote_point_to_top(model, X_1154)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1154 on the given reference triangle."""
    model = create_model('X_1154 = ISOGONAL CONJUGATE OF X_1141')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01154(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01154.json"))
    write_center_svg(
        model_acute,
        here / "x-01154.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
