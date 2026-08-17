# iPhone Testing Guide — B1 Label Studio Ultimate v4.1.1

This guide separates **general iPhone web-app validation** from **direct NIIMBOT B1 Bluetooth qualification** so that browser limitations are not confused with application failures.

## URLs

Once GitHub Pages is enabled and the deployment workflow succeeds:

- **B1 Label Studio:** https://tstrembu.github.io/niimbot-b1-label-studio/
- **iPhone compatibility check:** https://tstrembu.github.io/niimbot-b1-label-studio/compat.html

## Phase 1 — Safari: editor and export validation

Open the live B1 Label Studio URL in Safari and verify the non-Bluetooth parts of the application first.

Recommended checks:

1. Confirm the 40×20 mm starter canvas renders correctly and scrolls without clipping.
2. Build Text, QR, and Code 128 Quick Create labels.
3. Drag and multi-select elements; verify magnetic safe-area/center guides.
4. Rotate representative elements through 0°, 90°, 180°, and 270°.
5. Import/paste a small CSV dataset, insert tokens, switch preview records, and run selected-record preflight.
6. Exercise the six batch-range presets: First 10, First 50, Last 10, Last 50, All, Current → End.
7. Export PNG and **Pixel-Faithful SVG**.
8. Export/import Project JSON and verify the project returns with its layers/data intact.
9. Test Share PNG where the browser exposes file sharing.
10. Reload the page and confirm autosave/local template behavior as expected.

Use `compat.html` to see which browser capabilities are actually exposed by the current iPhone runtime.

## Phase 2 — Web Bluetooth browser: direct B1 qualification

Direct printing requires a runtime that exposes the Web Bluetooth API. On iPhone, open the same HTTPS GitHub Pages URL in a Web Bluetooth-capable browser such as **Bluefy – Web BLE Browser**.

Before connecting:

- Turn on Bluetooth in iOS.
- Power on the NIIMBOT B1 and keep it nearby.
- If the native NIIMBOT app is connected to the printer, disconnect/close it so it does not retain the BLE connection.
- Open `compat.html` first and confirm **Secure Context = Yes** and **Web Bluetooth API = Available** in the chosen runtime.
- Return to the main app and expand **Bluetooth & qualification diagnostics**.

### Connect

1. Tap **Connect B1**.
2. Select the NIIMBOT B1 from the Bluetooth chooser.
3. Wait for verification.
4. Do not proceed with direct-print qualification unless the app reports **B1 verified** and the diagnostics identify **model ID 4096**.
5. Record the detected protocol version and starting adaptive pace.

### Frozen qualification baseline

Do not change transport behavior during baseline qualification:

- Model ID: **4096 only**
- Resolution: **203 dpi**
- Bundle ceiling: **240 bytes fixed**
- Adaptive pacing: **10–40 ms**
- Idle heartbeat: **15 seconds**

The purpose of the physical tests is to measure this configuration, not tune it while testing.

## Physical sequence

Run the formal matrix in [`PHYSICAL_QUALIFICATION_PROTOCOL.md`](PHYSICAL_QUALIFICATION_PROTOCOL.md). A practical sequence is:

1. T01 Geometry & safe margins
2. T02 Typography bloom
3. T03 QR module resolution
4. T04 Code 128 scan benchmark
5. T05 Identical-copy repeatability
6. T06 Variable-data batching
7. T07 Mid-job cancellation
8. T08 Post-cancel recovery
9. T09 Idle keep-alive
10. T10 Background/resume
11. T11 Transparent media
12. T12 Multi-batch stability

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
Bundle ceiling shown:
Adaptive pace shown:
Heartbeat misses:
Page index:
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
- If raster rows are dropped or labels are incomplete, record the adaptive pace at failure before changing anything.
- If cancellation leaves the printer unusable until a power cycle, record T07 and T08 separately.
- If QR/Code 128 output prints cleanly but scans inconsistently, document physical module width, density, stock, and surface rather than treating that automatically as a transport failure.

## Code-freeze rule

v4.1.1 is the qualification candidate. Do not modify the QR engine, Code 128 engine, rasterizer, row RLE, page/task packet structure, 240-byte bundle ceiling, 10–40 ms pace range, heartbeat cadence, model gate, or cancellation architecture until physical evidence from the B1 indicates a specific change is warranted.
