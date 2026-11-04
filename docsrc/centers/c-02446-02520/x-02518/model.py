"""GEOMETOR construction model for X_2518 = RADICAL CENTER OF {BROCARD, MOSES, (X_4,2R)} CIRCLES."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_02518(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2518 = RADICAL CENTER OF {BROCARD, MOSES, (X_4,2R)} CIRCLES on reference triangle ABC."""
    X_2518 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) - c**(4))*(2*a**(4) + 2*b**(4) + 2*c**(4) - 3*b**(2)*c**(2)))', ID="X_2518", classes=["selected", "target"])
    X_211 = eval_trilinear_point(model, A, B, C, 'sin(A +  omega  )*(cos(B)*sin(B +  omega  ) + cos(C)*sin(C +  omega  ) - cos(A)*sin(A +  omega  ))', ID="X_211", classes=["center", "incident"])
    X_688 = eval_trilinear_point(model, A, B, C, '(a**(3)*(b**(4) - c**(4)))', ID="X_688", classes=["center", "incident"])
    central_line(model, X_211, X_688, 211, 688, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_2031 = eval_trilinear_point(model, A, B, C, '(2*sin(A - 3*omega  ) + (sin(omega)  )*(5*cos(A) + cos(A + 2*omega  )))', ID="X_2031", classes=["center", "incident"])
    central_line(model, X_512, X_2031, 512, 2031, incident=True)
    X_826 = eval_trilinear_point(model, A, B, C, 'a **(-1)*(b**(4) - c**(4)) + a**(3)*(b**(0) - c**(0))', ID="X_826", classes=["center", "incident"])
    X_2474 = eval_trilinear_point(model, A, B, C, '(a*(b**(4) - c**(4))*(a**(4) + b**(4) + c**(4) + 2*a**(2)*b**(2) + 2*a**(2)*c**(2) - 2*b**(2)*c**(2)))', ID="X_2474", classes=["center", "incident"])
    central_line(model, X_826, X_2474, 826, 2474, incident=True)
    return promote_point_to_top(model, X_2518)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2518 on the given reference triangle."""
    model = create_model('X_2518 = RADICAL CENTER OF {BROCARD, MOSES, (X_4,2R)} CIRCLES')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02518(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02518.json"))
    write_center_svg(
        model_acute,
        here / "x-02518.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
