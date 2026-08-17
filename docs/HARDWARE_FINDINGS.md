# Physical B1 Findings — Evidence Log

This record contains observations actually obtained from the physical NIIMBOT B1 qualification session. It distinguishes proven behavior from tests that remain pending.

## Environment observed

- Client: iPhone
- Direct-BLE runtime: Bluefy 3.9.3
- Hosting: GitHub Pages over secure HTTPS
- Web Bluetooth API: available in Bluefy
- Bluetooth adapter availability: yes
- Printer selected: `B1-H717032304`
- App identity result: **NIIMBOT B1**
- Model ID: **4096**
- Protocol: **3**
- Resolution: **203 dpi**
- Write API: `writeValueWithoutResponse`
- Bundle ceiling: **240 bytes fixed**
- Adaptive pace observed: **10 ms**
- Heartbeat misses observed: **0**

## S00 — End-to-end smoke print

Configuration observed in the app log:

- Raster: **320×160**
- Density: **3**
- Media ID: **1 / gap die-cut**
- Copies: **1**

Result: **PASS**

The printer completed the label without an application-reported error. The connection remained verified afterward.

During the run, the B1 emitted `0xD3 [0,159,1]`. On a 160-row raster, row 159 is the final zero-based row. v4.2.0 therefore surfaces this packet as read-only raster-row telemetry (`159 / 159 · complete · flag 1`) while retaining status polling as the authoritative job-completion path.

## Long verification URL QR proof

Payload tested:

`https://verify.janoshik.com/tests/84483-thymusin_alpha_1_10mg_T1M4QCH7NXAD`

Resolved geometry:

- UTF-8 bytes: **74**
- Error correction: **M**
- QR version: **5**
- QR matrix: **37×37 modules**
- Quiet zone: **4 modules per side**
- Printer module size: **3 dots/module**
- Printed QR extent: **135 dots / 16.9 mm**
- Density: **3**

Result: **single-label physical scan PASS**. Scanning the printed QR resolved to the intended verification URL.

This is sufficient evidence to remove the previous 2-dot default failure for similar URLs, but it is **not yet a repeatability qualification**. Multiple-label scan testing remains required before treating 3-dot Version-5 output as universally qualified across rolls, surfaces, firmware revisions, and devices.

## Current software consequence

v4.2.0 changes default QR sizing so a 40×20 QR + text label with 1.5 mm safe inset targets the full safe-area height. The 74-byte ECC-M proof URL therefore resolves automatically to the physically successful 135-dot / 3-dot-module geometry without manual resizing.

## Still pending

- Confirm physical roll dimensions before formal geometry/feed scoring.
- Multi-label 3-dot QR scan repeatability.
- T01–T12 formal qualification matrix, including feed geometry, typography, Code 128, identical copies, variable-data batches, cancellation/recovery, idle/background behavior, transparent media, and multi-batch stability.
