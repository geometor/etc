"""GEOMETOR construction model for X(231) = X(2)-CEVA CONJUGATE OF X(128)."""

from __future__ import annotations

from pathlib import Path

import sympy.geometry as spg
from geometor.model import Model

from geometor.etc.ops import (
    central_line,
    construct_baseline_triangle,
    create_model,
    eval_barycentric_point,
    eval_trilinear_point,
    orthocenter_of,
    promote_point_to_top,
    symmedian_point_of,
)
from geometor.etc.render import write_center_svg


def construct_x_00231(
    model: Model, A: spg.Point, B: spg.Point, C: spg.Point
) -> spg.Point:
    """Construct X(231) = X(2)-CEVA CONJUGATE OF X(128) on reference triangle ABC."""
    X_231 = eval_barycentric_point(model, A, B, C, '2*a**(8) - 4*a**(6)*b**(2) + 3*a**(4)*b**(4) - 2*a**(2)*b**(6) + b**(8) - 4*a**(6)*c**(2) + 2*a**(2)*b**(4)*c**(2) - 4*b**(6)*c**(2) + 3*a**(4)*c**(4) + 2*a**(2)*b**(2)*c**(4) + 6*b**(4)*c**(4) - 2*a**(2)*c**(6) - 4*b**(2)*c**(6) + c**(8)', ID="X(231)", classes=["selected", "target"])
    X_6 = symmedian_point_of(model, A, B, C, ID="X(6)", classes=["center", "incident"])
    X_17 = eval_trilinear_point(model, A, B, C, 'csc(A + pi /6)', ID="X(17)", classes=["center", "incident"])
    central_line(model, X_6, X_17, 6, 17, incident=True)
    X_4 = orthocenter_of(model, A, B, C, ID="X(4)", classes=["center", "incident"])
    X_96 = eval_trilinear_point(model, A, B, C, 'sec(2*A)*sec(B - C)', ID="X(96)", classes=["center", "incident"])
    central_line(model, X_4, X_96, 4, 96, incident=True)
    X_50 = eval_trilinear_point(model, A, B, C, 'sin(3*A)', ID="X(50)", classes=["center", "incident"])
    X_115 = eval_trilinear_point(model, A, B, C, 'b*c*(b**(2) - c**(2))**(2)', ID="X(115)", classes=["center", "incident"])
    central_line(model, X_50, X_115, 50, 115, incident=True)
    return promote_point_to_top(model, X_231)


def build_model(
    sides: tuple[float, float, float] = (5.0, 6.0, 7.0),
    show_guides: bool = False,
) -> Model:
    """Build a `geometor.model.Model` for X(231) on the given reference triangle."""
    model = create_model('X(231) = X(2)-CEVA CONJUGATE OF X(128)')
    A, B, C = construct_baseline_triangle(model, *sides, show_guides=show_guides)
    construct_x_00231(model, A, B, C)
    return model


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    model_acute = build_model((5.0, 6.0, 7.0))
    model_acute.save(str(here / "x-00231.json"))
    write_center_svg(
        model_acute,
        here / "x-00231.svg",
        subtitle="(a, b, c) = (5, 6, 7) | AB = 1",
    )
