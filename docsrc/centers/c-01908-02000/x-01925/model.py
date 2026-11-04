"""GEOMETOR construction model for X_1925 = CROSSSUM OF PU(13)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01925(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1925 = CROSSSUM OF PU(13) on reference triangle ABC."""
    X_1925 = eval_trilinear_point(model, A, B, C, '(1 + b**(2)*c**(2)/a**(4))', ID="X_1925", classes=["selected", "target"])
    X_92 = eval_trilinear_point(model, A, B, C, 'csc(2*A)', ID="X_92", classes=["center", "incident"])
    X_304 = eval_trilinear_point(model, A, B, C, '(cot(A))*(csc(A))**(2)', ID="X_304", classes=["center", "incident"])
    central_line(model, X_92, X_304, 92, 304, incident=True)
    X_76 = eval_trilinear_point(model, A, B, C, '1/a**(3)', ID="X_76", classes=["center", "incident"])
    X_335 = eval_trilinear_point(model, A, B, C, 'b*c/(a**(2) - b*c)', ID="X_335", classes=["center", "incident"])
    central_line(model, X_76, X_335, 76, 335, incident=True)
    X_469 = point_from_barycentrics(model, A, B, C, 0.14569854, 0.21687036, 0.6374311, ID="X_469", classes=["center", "incident"])
    X_1601 = point_from_barycentrics(model, A, B, C, 0.43272298, 0.23120612, 0.3360709, ID="X_1601", classes=["center", "incident"])
    central_line(model, X_469, X_1601, 469, 1601, incident=True)
    return promote_point_to_top(model, X_1925)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1925 on the given reference triangle."""
    model = create_model('X_1925 = CROSSSUM OF PU(13)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01925(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01925.json"))
    write_center_svg(
        model_acute,
        here / "x-01925.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
