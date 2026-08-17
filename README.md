# NIIMBOT B1 Label Studio Ultimate v4.2.0

A standalone, browser-based label designer and direct-print qualification build for the **NIIMBOT B1 (model ID 4096, 203 dpi)**.

## Live app

**https://tstrembu.github.io/niimbot-b1-label-studio/**

The GitHub Pages workflow reconstructs the verified v4.1.1 base, applies the evidence-driven v4.2.0 line patch, verifies the resulting artifact SHA-256, and only then deploys it as `index.html`.

**v4.2.0 SHA-256:** `236ef2ccf2159694dfdfdcefbb556b1014e658ab1c7e259082b41fbb1b9c97f7`

## Why v4.2.0 exists

Physical testing on an iPhone using Bluefy successfully connected to an actual B1, verified **model ID 4096 / protocol 3 / 203 dpi**, completed a one-label BLE print at the frozen 240-byte / 10–40 ms transport baseline, and successfully scanned a physical **74-byte, ECC-M, Version-5 QR at 3 dots/module**.

v4.2.0 uses that evidence to improve the default QR workflow for verification URLs in roughly the same length range instead of requiring manual resizing.

### QR production-profile improvements

- QR + text Quick Create uses the full 40×20 label safe-area height.
- A representative 74-byte ECC-M URL now resolves automatically to **Version 5 · 3 dots/module · 135 printed dots (16.9 mm)** instead of the prior 2-dot blocking condition.
- New QR elements default to the largest square that fits inside the active safe area.
- QR inspector includes **Maximize QR inside safe area**.
- Quick Create shows live QR byte count, version, dots/module, printed dots, and physical millimeters before rebuilding.
- The long QR/barcode payload field is a two-line textarea for easier iPhone editing.
- QR preflight keeps `<3 dots/module` as a blocking error, treats 3 dots/module as the minimum production profile requiring physical repeatability testing, and prefers 4+ when payload/layout permits.
- Text auto-fit warnings are de-duplicated so one final small-font condition produces one warning rather than two.
- Observed B1 `0xD3` raster-row packets are surfaced as read-only diagnostics; they do not replace the existing status-poll completion logic.

## iPhone use

The editor, templates, variable data, preflight, PNG/SVG export, JSON projects, QR generation, and Code 128 generation work as standard browser functionality on iPhone.

Direct B1 printing requires a runtime that exposes Web Bluetooth. Safari does not expose it; the physical proof used **Bluefy – Web BLE Browser** over the HTTPS GitHub Pages URL.

Compatibility diagnostics:

**https://tstrembu.github.io/niimbot-b1-label-studio/compat.html**

The compatibility page now reads `release-info.json` and displays the actually deployed version and SHA-256 alongside browser/Bluetooth capabilities.

## Qualified transport baseline

The v4.2.0 QR/UI refinements do **not** change the qualified transmit/print-task baseline:

- Target: NIIMBOT B1, model ID 4096
- Resolution: 203 dpi / practical 8 dots per mm
- BLE bundle ceiling: 240 bytes, fixed
- Adaptive write pacing: 10–40 ms
- Idle heartbeat: 15 seconds
- Model gate: direct printing is blocked unless model ID 4096 is verified
- QR matrix generator, binary master raster, RLE packetization, page/task sequencing, cancellation path, and Pixel-Faithful SVG conversion remain unchanged from v4.1.1

## Repository layout

- `release/v4.1.1/part*.b64` — losslessly compressed canonical v4.1.1 qualification base
- `release/v4.2.0/line-patch.json.gz.b64` — compact evidence-driven v4.2.0 line replacement payload
- `tools/apply_v420.py` — verifies the v4.1.1 base, applies the patch, then verifies the exact v4.2.0 SHA/byte count
- `docs/QA_RECORD_v4.2.0.md` — v4.2.0 QA and frozen-path record
- `docs/RELEASE_NOTES_v4.2.0.md` — change summary
- `docs/PHYSICAL_QUALIFICATION_PROTOCOL.md` — T01–T12 B1 hardware qualification matrix
- `docs/IPHONE_TESTING.md` — iPhone/Bluefy test instructions
- `.github/workflows/pages.yml` — integrity-verified GitHub Pages deployment

## Deployment integrity

The deployment fails rather than publishing if either the frozen v4.1.1 base hash or the resulting v4.2.0 hash/byte count differs from the expected values.

## Status

**v4.2.0 is the current evidence-driven qualification candidate.** The next software change should continue to be driven by physical B1 results, especially 3-dot QR repeatability, geometry/feed testing, batch behavior, cancellation/recovery, and longer-session stability.
