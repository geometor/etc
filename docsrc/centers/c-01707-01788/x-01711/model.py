"""GEOMETOR construction model for X_1711 = MIMOSA TRANSFORM OF X_19."""

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
    point_from_barycentrics,
    promote_point_to_top,
)
from geometor.etc.render import write_center_svg


def construct_x_01711(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_1711 = MIMOSA TRANSFORM OF X_19 on reference triangle ABC."""
    X_393 = eval_trilinear_point(model, A, B, C, 'b*c*(tan(A))**(2)', ID="X_393", classes=["center"])
    X_1 = incenter_of(model, A, B, C, ID="X_1", classes=["center"])
    X_1711 = ceva_conjugate(model, A, B, C, X_393, X_1, ID="X_1711", classes=["selected", "target"])
    X_9 = mittenpunkt_of(model, A, B, C, ID="X_9", classes=["center", "incident"])
    X_43 = eval_trilinear_point(model, A, B, C, 'a*b + a*c - b*c', ID="X_43", classes=["center", "incident"])
    central_line(model, X_9, X_43, 9, 43, incident=True)
    X_394 = eval_trilinear_point(model, A, B, C, 'cos(A)*cot(A)', ID="X_394", classes=["center", "incident"])
    central_line(model, X_1, X_394, 1, 394, incident=True)
    X_46 = eval_trilinear_point(model, A, B, C, 'cos(B) + cos(C) - cos(A)', ID="X_46", classes=["center", "incident"])
    X_407 = point_from_barycentrics(model, A, B, C, 0.10813862, 0.19355731, 0.69830407, ID="X_407", classes=["center", "incident"])
    central_line(model, X_46, X_407, 46, 407, incident=True)
    return promote_point_to_top(model, X_1711)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_1711 on the given reference triangle."""
    model = create_model('X_1711 = MIMOSA TRANSFORM OF X_19')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_01711(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-01711.json"))
    write_center_svg(
        model_acute,
        here / "x-01711.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
