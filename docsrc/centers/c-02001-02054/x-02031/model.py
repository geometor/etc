"""GEOMETOR construction model for X_2031 = RADICAL TRACE OF MOSES AND BROCARD CIRCLES."""

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
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02031(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2031 = RADICAL TRACE OF MOSES AND BROCARD CIRCLES on reference triangle ABC."""
    X_2031 = eval_trilinear_point(model, A, B, C, '(2*sin(A - 3*omega  ) + (sin(omega)  )*(5*cos(A) + cos(A + 2*omega  )))', ID="X_2031", classes=["selected", "target"])
    X_3 = circumcenter_of(model, A, B, C, ID="X_3", classes=["center", "incident"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    central_line(model, X_3, X_6, 3, 6, incident=True)
    X_230 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2)*(2*a**(2) - b**(2) - c**(2)) + (b**(2) - c**(2))**(2))', ID="X_230", classes=["center", "incident"])
    X_625 = eval_trilinear_point(model, A, B, C, '(2*(b**(4) + c**(4) - b**(2)*c**(2)) - a**(2)*(b**(2) + c**(2)))/a', ID="X_625", classes=["center", "incident"])
    central_line(model, X_230, X_625, 230, 625, incident=True)
    return promote_point_to_top(model, X_2031)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2031 on the given reference triangle."""
    model = create_model('X_2031 = RADICAL TRACE OF MOSES AND BROCARD CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02031(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02031.json"))
    write_center_svg(
        model_acute,
        here / "x-02031.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
