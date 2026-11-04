"""GEOMETOR construction model for X_836 = CROSSPOINT OF X_1 AND X_394."""

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
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_00836(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_836 = CROSSPOINT OF X_1 AND X_394 on reference triangle ABC."""
    X_836 = eval_trilinear_point(model, A, B, C, '(sin(B)*(sec(B))**(2) + sin(C)*(sec(C))**(2))', ID="X_836", classes=["selected", "target"])
    X_37 = eval_trilinear_point(model, A, B, C, 'b + c', ID="X_37", classes=["center", "incident"])
    X_73 = eval_trilinear_point(model, A, B, C, 'sec(B) + sec(C)', ID="X_73", classes=["center", "incident"])
    central_line(model, X_37, X_73, 37, 73, incident=True)
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center", "incident"])
    X_393 = eval_trilinear_point(model, A, B, C, 'b*c*(tan(A))**(2)', ID="X_393", classes=["center", "incident"])
    central_line(model, X_1, X_393, 1, 393, incident=True)
    X_820 = eval_trilinear_point(model, A, B, C, '((cos(A))**(2)*((cos(B))**(2) + (cos(C))**(2)))', ID="X_820", classes=["center", "incident"])
    X_1100 = eval_trilinear_point(model, A, B, C, '2*a + b + c', ID="X_1100", classes=["center", "incident"])
    central_line(model, X_820, X_1100, 820, 1100, incident=True)
    return promote_point_to_top(model, X_836)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_836 on the given reference triangle."""
    model = create_model('X_836 = CROSSPOINT OF X_1 AND X_394')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00836(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00836.json"))
    write_center_svg(
        model_acute,
        here / "x-00836.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
