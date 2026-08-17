# NIIMBOT B1 — v4.2.0 Physical Qualification Protocol

**Software baseline:** B1 Label Studio Ultimate v4.2.0  
**Printer target:** NIIMBOT B1, model ID 4096, 203 dpi  
**Transport baseline:** 240-byte fixed bundle ceiling; adaptive 10–40 ms pacing; 15-second idle heartbeat.  
**Evidence entering this protocol:** single-label BLE print PASS and a physical Version-5 / ECC-M / 3-dot-module / 74-byte QR scan PASS. See [`HARDWARE_FINDINGS.md`](HARDWARE_FINDINGS.md).

> The acceptance values below are qualification targets for this test program unless independently documented as manufacturer specifications.

| Test | Scenario | Configuration / inputs | Qualification target |
|---|---|---|---|
| T01 | Geometry & safe margins | 10 × labels matching the confirmed physical roll dimensions, density 3, perimeter border | No die-cut clipping; observed feed offset ≤0.5 mm target |
| T02 | Typography bloom | 14/16/18/20/24-dot text at densities 2/3/4/5 | 14-dot text legible at density 3; document bloom at density 5 |
| T03 | QR module resolution + common URL repeatability | (A) common ~70–80-byte URL, ECC M, Version ~5, 3 dots/module, density 3, 10 labels; (B) shorter payloads at 3 vs 4 dots/module where geometry permits | All common-profile labels decode to the exact intended URL; record acquisition speed/device/distance and any failures |
| T04 | Code 128 scan benchmark | Numeric + alphanumeric; 1- vs 2-dot narrow modules | Record decode reliability by laser/camera scanner |
| T05 | Identical-copy repeatability | 25 copies using one raster upload, copies=25 | Correct gap/cut stop on all labels; no dropped raster rows |
| T06 | Variable-data batching | 25 distinct CSV records | Correct sequence; no missing/duplicated records or buffer failure |
| T07 | Mid-job cancellation | Cancel near page 12 of 25 | Queued writes terminate; printer stops promptly; record actual overrun |
| T08 | Post-cancel recovery | Print one normal label immediately after T07 | Clean new job without power cycle |
| T09 | Idle keep-alive | 10 minutes connected, no print | Record connection retention and heartbeat misses |
| T10 | Background / resume | Background browser ~60 s, return, print | Clean resume/reconnect or clear error; no UI freeze |
| T11 | Transparent media | Media ID 5 on representative light/dark surfaces | Sensor/feed behavior documented; QR/barcode contrast scan-tested |
| T12 | Multi-batch stability | Three consecutive 15-label batches | No packet drops; memory/UI stable; record final adaptive pace |

## Per-run record

```text
Run Date/Time:      ______________________________
Software Build:     v4.2.0
Device / OS:        ______________________________
Browser / Runtime:  ______________________________
Printer Model ID:   4096 / other: _______________
Protocol Version:   ______________________________
Firmware (if known):______________________________
Label Media / Size: ______________________________
Media ID:           1 / 2 / 5
Print Density:      1 / 2 / 3 / 4 / 5

QR telemetry (when relevant)
  Payload bytes:    ______
  QR version:       ______
  ECC:              ______
  Dots/module:      ______
  Printed QR dots:  ______

Transport telemetry
  Bundle ceiling:   240 bytes (fixed)
  Starting pace:    ______ ms
  Ending pace:      ______ ms
  Max pace seen:    ______ ms
  Heartbeat misses: ______
  Page index end:   ______
  Last raster row:  ______________________________
  Printer errors:   ______________________________

Tests run:          T__ T__ T__ T__
Result:             PASS / FAIL / PARTIAL

Physical observations:
__________________________________________________
__________________________________________________

Scan results / devices:
__________________________________________________

Failure page / recovery behavior (if applicable):
__________________________________________________
__________________________________________________
```

## Qualification decision

- **PASS / freeze v4.2.0:** __________________________________________
- **Small corrective patch → v4.2.1:** ______________________________
- **Behavioral revision → v4.3:** ___________________________________

Tester: ____________________________   Date: _________________________
