# iPhone Testing Guide — B1 Label Studio Ultimate v4.2.0

This guide separates **general iPhone web-app validation** from **direct NIIMBOT B1 Bluetooth qualification** so that browser limitations are not confused with application failures.

## URLs

- **B1 Label Studio:** https://tstrembu.github.io/niimbot-b1-label-studio/
- **iPhone compatibility check:** https://tstrembu.github.io/niimbot-b1-label-studio/compat.html

The compatibility page reports the actually deployed release version/SHA along with browser capabilities.

## Phase 1 — Safari: editor and export validation

Open the live B1 Label Studio URL in Safari and verify the non-Bluetooth parts of the application first.

Recommended checks:

1. Confirm the 40×20 mm starter canvas renders correctly and scrolls without clipping.
2. Build Text, QR, and Code 128 Quick Create labels.
3. For a verification URL near the tested ~74-byte length, confirm the QR + text layout reports approximately **Version 5 · 3 dots/module · 135 printed dots** at ECC M rather than a blocking 2-dot result.
4. Drag and multi-select elements; verify magnetic safe-area/center guides.
5. Rotate representative elements through 0°, 90°, 180°, and 270°.
6. Import/paste a small CSV dataset, insert tokens, switch preview records, and run selected-record preflight.
7. Exercise the six batch-range presets: First 10, First 50, Last 10, Last 50, All, Current → End.
8. Export PNG and **Pixel-Faithful SVG**.
9. Export/import Project JSON and verify the project returns with its layers/data intact.
10. Test Share PNG where the browser exposes file sharing.
11. Reload the page and confirm autosave/local template behavior as expected.

Use `compat.html` to see which browser capabilities are actually exposed by the current iPhone runtime.

## Phase 2 — Web Bluetooth browser: direct B1 qualification

Direct printing requires a runtime that exposes the Web Bluetooth API. The successful physical proof used **Bluefy 3.9.3** on iPhone over the HTTPS GitHub Pages URL.

Before connecting:

- Turn on Bluetooth in iOS.
- Power on the NIIMBOT B1 and keep it nearby.
- If the native NIIMBOT app is connected to the printer, disconnect/close it so it does not retain the BLE connection.
- Open `compat.html` first and confirm **Secure Context = Yes**, **Web Bluetooth API = Available**, and **Bluetooth availability = Yes** in the chosen runtime.
- Return to the main app and expand **Bluetooth & qualification diagnostics**.

### Connect

1. Tap **Connect B1**.
2. Select the NIIMBOT B1 from the Bluetooth chooser.
3. Wait for verification.
4. Do not proceed with direct-print qualification unless the app reports **B1 verified** and the diagnostics identify **model ID 4096**.
5. Record the detected protocol version and starting adaptive pace.

### Qualified transport baseline

Do not change transport behavior during qualification:

- Model ID: **4096 only**
- Resolution: **203 dpi**
- Bundle ceiling: **240 bytes fixed**
- Adaptive pacing: **10–40 ms**
- Idle heartbeat: **15 seconds**

The purpose of the physical tests is to measure this configuration, not tune it while testing.

### Evidence already observed

The initial physical session established:

- Model ID **4096**, protocol **3**, 203 dpi verification.
- `writeValueWithoutResponse` transport.
- 240-byte bundle ceiling, **10 ms** observed pace, **0 heartbeat misses**.
- Successful 320×160 / density-3 / media-1 / one-copy job.
- `0xD3 [0,159,1]` observed during the 160-row proof; v4.2.0 now shows this as read-only last-raster-row telemetry.
- Successful physical scan of the 74-byte Janoshik verification URL at **Version 5 / ECC M / 3 dots per module / 135 printed dots**.

See [`HARDWARE_FINDINGS.md`](HARDWARE_FINDINGS.md) for the evidence log.

## Physical sequence

Continue with the formal matrix in [`PHYSICAL_QUALIFICATION_PROTOCOL.md`](PHYSICAL_QUALIFICATION_PROTOCOL.md). A practical sequence is:

1. Confirm the physical roll dimensions.
2. T01 Geometry & safe margins
3. T02 Typography bloom
4. T03 QR module resolution and common long-URL repeatability
5. T04 Code 128 scan benchmark
6. T05 Identical-copy repeatability
7. T06 Variable-data batching
8. T07 Mid-job cancellation
9. T08 Post-cancel recovery
10. T09 Idle keep-alive
11. T10 Background/resume
12. T11 Transparent media
13. T12 Multi-batch stability

Start with inexpensive/small runs before the 25-label stress tests.

## What to capture if anything fails

Before reconnecting, reloading, or power-cycling, record as much of the following as possible:

```text
Test ID:
Browser / runtime:
iPhone model / iOS version:
Printer model ID:
Detected protocol:
Media ID / physical stock:
Density:
QR payload bytes/version/dots per module (if relevant):
Bundle ceiling shown:
Adaptive pace shown:
Heartbeat misses:
Page index:
Last raster row telemetry:
Pending acknowledgements:
Write queue epoch:
Printer error packet / UI error:
Expected result:
Actual physical result:
Failure label/page number:
Did a one-label recovery job work without power-cycling?:
```

A screenshot of the diagnostics/log area is especially useful.

## Interpreting failures

- If the browser does not expose `navigator.bluetooth`, that is a runtime capability result rather than a B1 protocol failure.
- If the app connects but blocks printing because the model ID is not 4096, keep the block in place and record the detected identity.
- If raster rows are dropped or labels are incomplete, record the adaptive pace and **Last raster row telemetry** at failure before changing anything.
- `0xD3` telemetry is diagnostic evidence only; the app still uses status polling for print completion.
- If cancellation leaves the printer unusable until a power cycle, record T07 and T08 separately.
- If QR/Code 128 output prints cleanly but scans inconsistently, document physical module width, density, stock, and surface rather than treating that automatically as a transport failure.

## Code-freeze rule

v4.2.0 is the current evidence-driven qualification candidate. Do not modify the QR matrix generator, Code 128 engine, rasterizer, row RLE, page/task packet structure, 240-byte bundle ceiling, 10–40 ms pace range, heartbeat cadence, model gate, or cancellation architecture until physical evidence from the B1 indicates a specific change is warranted.
