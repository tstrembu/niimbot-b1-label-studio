# NIIMBOT B1 Label Studio Ultimate v4.2.0 — QR Production Profile QA Record

**Artifact:** `NIIMBOT_B1_Label_Studio_Ultimate_v4.2.0.html`  
**Release intent:** evidence-driven behavioral refinement following successful physical B1/iPhone/Bluefy printing and QR scan testing. BLE transport, print-task sequencing, canonical QR encoding, rasterization, and direct-print packet behavior remain unchanged from v4.1.1.  
**SHA-256:** `236ef2ccf2159694dfdfdcefbb556b1014e658ab1c7e259082b41fbb1b9c97f7`  
**Bytes:** `180454`

## Physical evidence that motivated v4.2.0

The qualification work on a physical NIIMBOT B1 established the following user-observed baseline before this revision:

- iPhone + Bluefy exposed Web Bluetooth in the GitHub Pages HTTPS runtime.
- B1 Label Studio verified **NIIMBOT B1 · model ID 4096 · protocol 3 · 203 dpi**.
- The transport remained at **240-byte bundle ceiling / 10 ms active pace / 0 heartbeat misses** during the single-label proof.
- A **320×160, density-3, media-1, one-copy** job completed successfully.
- The log received unsolicited `0xd3 [0,159,1]` during that proof and then reported `print complete`.
- A physical **Version 5 / ECC M / 3 dots per module / 135-dot / 74-byte** QR printed successfully and scanned to the intended verification URL.

These observations justify optimizing defaults for the common ~70–80-byte URL use case while preserving the qualified transport baseline.

## Implemented v4.2.0 changes

- **QR + text Quick Create now targets the full 1.5 mm safe-area height** on 40×20 stock. For the 74-byte proof URL this resolves automatically to Version 5, 3 dots/module, 135 printed dots; manual resizing is no longer required.
- **New QR elements default to the largest square target available inside the active safe area.** Actual rendered QR dimensions remain exact integer-module multiples.
- Added **Maximize QR inside safe area** in the QR inspector. It sets the safe-area target and clamps the QR back inside the safe inset.
- Quick Create's long QR/barcode payload field is now a **two-line textarea** for better iPhone editing.
- Added **live Quick Create QR geometry metadata** showing EC level, byte count, version, dots/module, printed dots, and millimeters before rebuilding the label.
- Slightly widened the right-hand text region in the QR + text 40×20 template from 148 to 154 dots while retaining the 12-dot right safe inset and a 7-dot gap from a 135-dot QR.
- Refined QR preflight: fewer than 3 dots/module remains a blocking error; 3 dots/module is one production warning with repeatability guidance; the redundant generic “Version 3+ is dense” warning was removed.
- QR payload-length warning now begins above 96 UTF-8 bytes, where shortening is more likely to improve module size for this layout.
- Text preflight now combines “small text” and “auto-fit reduced” into one warning instead of emitting two warnings for the same final font size.
- SOP copy now records the physically scan-proven 40×20, EC-M, 3-dot QR profile without claiming universal stock/firmware qualification.

## Automated validation

`test_v420.py` completed **13/13 checks**:

1. HTML parses and all DOM IDs are unique (**127 / 127**).
2. No external runtime script dependencies.
3. Version identifiers are consistently v4.2.0.
4. The entire B1 BLE transport block is byte-for-byte unchanged from v4.1.1.
5. The supplied 74-byte verification URL defaults to Version 5 / 3 dots per module / 135 printed dots.
6. The representative `Thymosin Alpha-1` QR + text Quick Create label has **0 preflight errors**.
7. Text auto-fit warnings are de-duplicated.
8. Short `https://example.com` payloads retain at least 4 dots/module.
9. A newly added QR uses the safe-area target by default.
10. Quick payload editor is a textarea.
11. Live Quick QR metadata correctly reports the 74-byte Version-5 / 3-dot geometry.
12. Maximize-QR control keeps the resulting QR inside the safe area.
13. The widened QR + text region avoids measured text overflow in the browser QA case.

Both embedded JavaScript blocks pass `node --check`.

## Frozen transport / rendering confirmation

The following remain unchanged from v4.1.1:

- BLE service/characteristic UUIDs
- `BLE_BUNDLE_MAX=240`
- `PACE_MIN=10`
- `PACE_MAX=40`
- `HEARTBEAT_INTERVAL=15000`
- model-ID 4096 hard gate
- `qrPayloadInfo`, `qrMatrix`, `qrLayout`
- `localElementCanvas`, `renderedElementCanvas`
- `toBitmap`
- `sendBitmapRows`
- `beginPrintTask`, `sendOnePage`
- `printJob`, `printDistinctBatch`, `cancelPrint`
- `bitmapToSvg`

This release changes **QR defaults, layout ergonomics, and preflight messaging**, not the encoded QR matrix or B1 transport.

## Visual QA

A 430-pixel mobile Chromium render was inspected after the final changes. The main 40×20 canvas, enlarged QR, right-side text, mobile textarea, live QR metadata, and surrounding controls rendered without clipping or overlap in the inspected views.

## Remaining physical acceptance

v4.2.0 should be re-proved on the physical B1 using the common long-URL profile, then continue through T01–T12. In particular, the 3-dot QR profile now needs repeatability testing across multiple labels rather than relying on one successful scan.
