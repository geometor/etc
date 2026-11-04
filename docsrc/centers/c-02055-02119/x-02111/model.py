"""GEOMETOR construction model for X_2111 = X_2-ISOCONJUGATE OF X_2110."""

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


def construct_x_02111(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2111 = X_2-ISOCONJUGATE OF X_2110 on reference triangle ABC."""
    X_2111 = eval_trilinear_point(model, A, B, C, '(1/((b**(2) + b*c + c**(2))*a**(3) - (b + c)*(b**(2) + c**(2))*a**(2) - b*c*(b**(2) - b*c + c**(2))*a + b**(2)*c**(2)*(b + c)))', ID="X_2111", classes=["selected", "target"])
    X_239 = eval_trilinear_point(model, A, B, C, 'b*c*(a**(2) - b*c)', ID="X_239", classes=["center", "incident"])
    X_672 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) + c**(2) - a*(b + c))', ID="X_672", classes=["center", "incident"])
    central_line(model, X_239, X_672, 239, 672, incident=True)
    X_238 = eval_trilinear_point(model, A, B, C, 'a**(2) - b*c', ID="X_238", classes=["center", "incident"])
    X_2110 = eval_trilinear_point(model, A, B, C, '(a*((b**(2) + b*c + c**(2))*a**(3) - (b + c)*(b**(2) + c**(2))*a**(2) - b*c*(b**(2) - b*c + c**(2))*a + b**(2)*c**(2)*(b + c)))', ID="X_2110", classes=["center", "incident"])
    central_line(model, X_238, X_2110, 238, 2110, incident=True)
    X_2106 = eval_trilinear_point(model, A, B, C, '((a + b)*(a + c)*(b**(2)*c**(2) - a**(2)*b**(2) - a**(2)*c**(2) + a*b*c*(b + c - a)))', ID="X_2106", classes=["center", "incident"])
    X_2112 = eval_trilinear_point(model, A, B, C, '(a*(a**(4) - b*c*a**(2) - (b**(3) + c**(3))*a + 2*b**(2)*c**(2)))', ID="X_2112", classes=["center", "incident"])
    central_line(model, X_2106, X_2112, 2106, 2112, incident=True)
    return promote_point_to_top(model, X_2111)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2111 on the given reference triangle."""
    model = create_model('X_2111 = X_2-ISOCONJUGATE OF X_2110')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02111(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02111.json"))
    write_center_svg(
        model_acute,
        here / "x-02111.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
