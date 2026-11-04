"""GEOMETOR construction model for X_2440 = ISOGONAL CONJUGATE OF X_2414."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_trilinear_point,
    isogonal_conjugate,
    point_from_barycentrics,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_02440(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X_2440 = ISOGONAL CONJUGATE OF X_2414 on reference triangle ABC."""
    X_2414 = point_from_barycentrics(model, A, B, C, 1.6475771, -0.04845815, -0.59911894, ID="X_2414", classes=["center"])
    X_2440 = isogonal_conjugate(model, A, B, C, X_2414, ID="X_2440", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X_6", classes=["center", "incident"])
    X_513 = eval_trilinear_point(model, A, B, C, 'b - c', ID="X_513", classes=["center", "incident"])
    central_line(model, X_6, X_513, 6, 513, incident=True)
    X_512 = eval_trilinear_point(model, A, B, C, 'a*(b**(2) - c**(2))', ID="X_512", classes=["center", "incident"])
    X_884 = point_from_barycentrics(model, A, B, C, -0.045819015, 0.98969072, 0.056128293, ID="X_884", classes=["center", "incident"])
    central_line(model, X_512, X_884, 512, 884, incident=True)
    X_919 = point_from_barycentrics(model, A, B, C, -0.11560694, 0.83236994, 0.28323699, ID="X_919", classes=["center", "incident"])
    X_2427 = point_from_barycentrics(model, A, B, C, -0.83333333, 0.2, 1.6333333, ID="X_2427", classes=["center", "incident"])
    central_line(model, X_919, X_2427, 919, 2427, incident=True)
    return promote_point_to_top(model, X_2440)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X_2440 on the given reference triangle."""
    model = create_model('X_2440 = ISOGONAL CONJUGATE OF X_2414')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_02440(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-02440.json"))
    write_center_svg(
        model_acute,
        here / "x-02440.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
