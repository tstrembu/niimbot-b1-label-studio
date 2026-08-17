# NIIMBOT B1 Label Studio Ultimate v4.1.1 — Qualification-Prep QA Record

**Artifact:** `NIIMBOT_B1_Label_Studio_Ultimate_v4.1.1.html`  
**Release intent:** narrowly scoped qualification-prep patch over v4.1; no intentional change to canonical rendering, encoding, rasterization, or B1 print-task behavior.  
**SHA-256:** `b0e454f0d5720ddc24c5ce6c3ec616ad20a1cada854eb7aa40918abea5ccdb52`

## Implemented v4.1.1 changes

- Added six quick batch-range presets: **First 10, First 50, Last 10, Last 50, All, Current → End**.
- Range presets preserve active field/text filters and explicitly invalidate `batch.lastPreflight`.
- Renamed SVG output to **Export Pixel-Faithful SVG** and clarified that it converts the canonical 1-bit thermal raster into physical-dimension `<rect>` runs rather than semantic editable objects.
- Expanded SOP copy to distinguish PNG, Pixel-Faithful SVG, and Project JSON roles.
- Added read-only **Bluetooth & qualification diagnostics** showing B1 identity, protocol, GATT state, write API, fixed 240-byte bundle ceiling, current adaptive pace, 10–40 ms pace range, 15 s heartbeat interval, heartbeat misses, secure-context state, page index, pending acknowledgements, write queue epoch, and media/density.
- Added a qualification-baseline log entry after B1 model-ID 4096 verification.
- Extracted the existing 15-second heartbeat literal to `HEARTBEAT_INTERVAL=15000` without changing behavior.

## Static and syntax validation

- HTML parsed successfully with BeautifulSoup.
- **126 DOM IDs / 126 unique IDs**; no duplicates detected.
- No external runtime `<script src>` dependencies.
- Both embedded JavaScript blocks pass `node --check`.
- Frozen transport constants verified:
  - `BLE_BUNDLE_MAX=240`
  - `PACE_MIN=10`
  - `PACE_MAX=40`
  - `HEARTBEAT_INTERVAL=15000`
- B1-only hard gate remains `printerModelId !== 4096` → direct print blocked.

## Frozen-core comparison against v4.1

The following function bodies were extracted and SHA-compared between v4.1 and v4.1.1; all were **byte-for-byte unchanged**:

- `textLayout`
- `qrMatrix`
- `qrLayout`
- `encodeCode128`
- `barcodeLayout`
- `normalizeRotation`
- `toBitmap`
- `processedImageCanvas`
- `renderedElementCanvas`
- `sendBitmapRows`
- `beginPrintTask`
- `sendOnePage`
- `printJob`
- `printDistinctBatch`
- `cancelPrint`
- `bitmapToSvg`

This confirms the qualification-prep patch did not alter the core encoding, layout, raster, print-task, cancellation, or SVG conversion implementations.

## Batch-range logic checks

The implemented preset mapping is:

- `first10`: `1 → min(10, N)`
- `first50`: `1 → min(50, N)`
- `last10`: `max(1, N-9) → N`
- `last50`: `max(1, N-49) → N`
- `all`: `1 → N`
- `fromCurrent`: `min(N, currentIndex+1) → N`

The handler does not modify `filterField` or `filterText`, so active filtering is preserved.

## Rendering / browser note

A container-headless Chromium screenshot attempt could not complete because the sandbox Chromium process stalled on its system D-Bus/browser environment. This is an environment limitation and is **not counted as a browser-runtime pass**. Syntax/static validation above completed successfully.

## Hardware boundary

No physical NIIMBOT B1 was available in the execution environment. Direct BLE, feed alignment, scan reliability, cancellation recovery, keep-alive behavior, and long-session stability remain subject to the physical T01–T12 qualification protocol.
