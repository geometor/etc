"""Integrity tests for generated exact symbolic ETC JSON shards."""

from __future__ import annotations

import json
import math

import pytest

from geometor.etc.shards import DEFAULT_DATA_DIR

MANIFEST_PATH = DEFAULT_DATA_DIR / "manifest.json"


@pytest.mark.skipif(not MANIFEST_PATH.is_file(), reason="Shards not yet generated in .cache/etc_data")
def test_manifest_and_shards_integrity() -> None:
    """Verify manifest metadata, shard completeness, search index, and collinearity audit."""
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    assert manifest["schema"] == 1
    assert manifest["total_centers"] >= 4000
    assert len(manifest["triangles"]) == 7

    # Exact algebraic rate on Heronian & Kimberling should exceed 90%
    h_stats = manifest["stats"]["heronian"]
    assert h_stats["exact"] / manifest["total_centers"] >= 0.90

    # Exact projective collinearity proof pass rate >= 97%
    k_audit = manifest["collinearity_audits"]["kimberling"]
    assert k_audit["tested_centers"] >= 3000
    assert k_audit["passed_centers"] / k_audit["tested_centers"] >= 0.97

    # Search index matches total centers and is sorted ascending
    search_rows = json.loads((DEFAULT_DATA_DIR / "search-index.json").read_text(encoding="utf-8"))
    assert len(search_rows) == manifest["total_centers"]
    nums = [r[0] for r in search_rows]
    assert nums == sorted(nums)

    # Core centers lookup contains all foundational hubs X_1..X_19
    core = json.loads((DEFAULT_DATA_DIR / "core-centers.json").read_text(encoding="utf-8"))
    for k in range(1, 20):
        assert str(k) in core
        assert "heronian" in core[str(k)]["xy"]

    # Spot-check shard 1 (X_1, X_2, X_10, X_20, X_100) and shard 40 (X_3901, X_4000)
    s1 = json.loads((DEFAULT_DATA_DIR / "shards" / "s-00001-00100.json").read_text(encoding="utf-8"))
    for k in ("1", "2", "10", "20", "100"):
        c = s1["centers"][k]
        assert c["n"] == int(k)
        assert "heronian" in c["tris"]
        assert c["tris"]["heronian"]["p"] == "e"
        assert c["tris"]["heronian"]["st"] == "f"
        xy = c["tris"]["heronian"]["xy"]
        assert len(xy) == 2 and all(math.isfinite(v) for v in xy)

    # X_2 Centroid exact Heronian coordinates: (19/3, 4)
    x2_xy = s1["centers"]["2"]["tris"]["heronian"]["xy"]
    assert abs(x2_xy[0] - 19.0 / 3.0) < 1e-5
    assert abs(x2_xy[1] - 4.0) < 1e-5

    # X_10 Spieker Center exact Heronian coordinates: (13/2, 4)
    x10_xy = s1["centers"]["10"]["tris"]["heronian"]["xy"]
    assert abs(x10_xy[0] - 6.5) < 1e-5
    assert abs(x10_xy[1] - 4.0) < 1e-5

    s40 = json.loads((DEFAULT_DATA_DIR / "shards" / "s-03901-04000.json").read_text(encoding="utf-8"))
    assert "3901" in s40["centers"]
    assert "4000" in s40["centers"]

    if manifest["total_centers"] >= 73_000:
        assert manifest["total_centers"] == manifest["max_center"]
        assert nums == list(range(1, manifest["max_center"] + 1))
        for check_n in (50_000, 57_621, 57_622, 60_349, 68_618, 71_412, 73_310):
            s_start = ((check_n - 1) // 100) * 100 + 1
            s_end = s_start + 99
            spath = DEFAULT_DATA_DIR / "shards" / f"s-{s_start:05d}-{s_end:05d}.json"
            sdata = json.loads(spath.read_text(encoding="utf-8"))
            assert str(check_n) in sdata["centers"]
            rec = sdata["centers"][str(check_n)]
            assert rec["n"] == check_n
            assert "heronian" in rec["tris"]
            assert rec["tris"]["heronian"]["p"] in {"e", "m"}

    families_path = DEFAULT_DATA_DIR / "families.json"
    if families_path.is_file():
        fdata = json.loads(families_path.read_text(encoding="utf-8"))
        assert fdata["schema"] == 1
        assert len(fdata["collections"]) == 62
        assert len(fdata["families"]) >= 900
        assert fdata["collections"][0]["slug"] == "c-00001-00019"
        assert fdata["collections"][0]["start"] == 1
        assert fdata["collections"][0]["end"] == 19
        assert fdata["collections"][1]["slug"] == "c-00020-00030"
        assert fdata["families"][0]["id"] == "f-0001"

