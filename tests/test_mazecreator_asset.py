"""mazeCreator_v0.3.swf (M2) -- shipped rebuild asset sanity.

The SWF is a rebuild (M2): logic pinned by the oracle gates
(oracle/editor-roundtrip, oracle/editor-visual), pixels redrawn from the
'Making a maze.png' screenshot. This test pins the shipping artifact:
embed-contract header facts + provenance bookkeeping.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from swf_header import read_header

SWF = ROOT / "srv" / "includes" / "mazeCreator_v0.3.swf"


def test_swf_matches_embed_contract():
    # srv/index.php:3617 embeds 688x400 player 8; siblings run 25fps
    h = read_header(SWF)
    assert h["version"] == 8
    assert (h["w"], h["h"]) == (688, 400)
    assert h["fps"] == 25


def test_provenance_sidecar_and_ledger():
    sidecar = SWF.parent / (SWF.name + ".provenance")
    text = sidecar.read_text()
    assert "M2" in text and "DO NOT PROMOTE" in text
    row = [l for l in (ROOT / "LEDGER.tsv").read_text(encoding="utf-8").splitlines()
           if l.startswith("srv/includes/mazeCreator_v0.3.swf\t")]
    assert len(row) == 1
    assert "\tM2\t" in row[0]


def test_editor_source_headers():
    src = (ROOT / "src" / "mazecreator" / "Editor.as").read_text()
    assert "M2" in src and "srv/index.php" in src
