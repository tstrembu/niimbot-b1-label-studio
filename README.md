# NIIMBOT B1 Label Studio Ultimate v4.1.1

A standalone, browser-based label designer and direct-print qualification build for the **NIIMBOT B1 (model ID 4096, 203 dpi)**.

## Live app

Once GitHub Pages is enabled with **Settings → Pages → Source: GitHub Actions**, the deployed app is available at:

**https://tstrembu.github.io/niimbot-b1-label-studio/**

The Pages workflow reconstructs the exact frozen v4.1.1 HTML from the compressed release payload, verifies its SHA-256, and deploys that verified file as `index.html`.

**Frozen source SHA-256:** `b0e454f0d5720ddc24c5ce6c3ec616ad20a1cada854eb7aa40918abea5ccdb52`

## iPhone use

The editor, templates, variable data, preflight, PNG/SVG export, JSON projects, QR generation, and Code 128 generation can be tested as normal web functionality on iPhone.

Direct B1 printing uses the Web Bluetooth API. The site must be loaded over HTTPS and the browser/runtime must expose `navigator.bluetooth`. If Bluetooth controls are unavailable in Safari, open the same GitHub Pages URL in a Web Bluetooth-capable iOS browser such as **Bluefy – Web BLE Browser**, then run the physical qualification protocol.

See [`docs/IPHONE_TESTING.md`](docs/IPHONE_TESTING.md) for the recommended iPhone test sequence.

## Qualification baseline

- Target: NIIMBOT B1, model ID 4096
- Resolution: 203 dpi / practical 8 dots per mm
- BLE bundle ceiling: 240 bytes, fixed
- Adaptive write pacing: 10–40 ms
- Idle heartbeat: 15 seconds
- Model gate: direct printing is blocked unless model ID 4096 is verified
- Release intent: qualification-prep only; core rendering, encoding, rasterization, and print-task behavior are frozen from v4.1

## Repository layout

- `release/NIIMBOT_B1_Label_Studio_Ultimate_v4.1.1.html.gz.b64` — lossless compressed canonical release payload
- `docs/QA_RECORD.md` — software QA and frozen-core record
- `docs/PHYSICAL_QUALIFICATION_PROTOCOL.md` — T01–T12 B1 hardware qualification matrix
- `docs/IPHONE_TESTING.md` — iPhone/Bluefy test instructions
- `.github/workflows/pages.yml` — SHA-verified GitHub Pages deployment

## Deployment integrity

The workflow decodes the canonical payload with `base64` + `gzip`, verifies the decoded HTML against the frozen SHA-256, and only then uploads it to GitHub Pages. A hash mismatch fails the deployment instead of publishing modified code.

## Status

**v4.1.1 is the frozen qualification candidate.** Any v4.1.2 or v4.2 change should be driven by results from physical B1 testing rather than speculative transport changes.
