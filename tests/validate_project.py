"""Lightweight checks for the analog design portfolio repo."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


EXPECTED_FILES = [
    "README.md",
    "op-amp-design/README.md",
    "op-amp-design/op_amp_calculations.ipynb",
    "op-amp-design/2OPAMP.asc",
    "op-amp-design/AC.asc",
    "op-amp-design/ICMR.asc",
    "op-amp-design/NOISE.asc",
    "op-amp-design/OUTPUT SWING.asc",
    "op-amp-design/SLEW RATE.asc",
    "op-amp-design/op_amp_design_report.pdf",
    "filter-design/README.md",
    "filter-design/filter_calculations.ipynb",
    "filter-design/LPF.asc",
    "filter-design/onepole.asy",
    "filter-design/OPAMP.sub",
    "filter-design/filter_design_report.pdf",
]


def test_expected_files_exist():
    missing = [path for path in EXPECTED_FILES if not (ROOT / path).exists()]
    assert not missing, f"Missing expected files: {missing}"


def test_notebooks_are_valid_json():
    for notebook in ROOT.rglob("*.ipynb"):
        data = json.loads(notebook.read_text(encoding="utf-8"))
        assert "cells" in data, notebook


def test_ltspice_paths_are_portable():
    text = (ROOT / "filter-design" / "onepole.asy").read_text(encoding="utf-8")
    assert "C:\\" not in text
    assert "OPAMP.sub" in text


if __name__ == "__main__":
    tests = [
        test_expected_files_exist,
        test_notebooks_are_valid_json,
        test_ltspice_paths_are_portable,
    ]

    for test in tests:
        test()
        print(f"PASS {test.__name__}")
