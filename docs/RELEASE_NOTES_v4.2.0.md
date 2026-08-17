# B1 Label Studio Ultimate v4.2.0 — Release Notes

v4.2.0 is the first revision driven directly by physical B1/iPhone/Bluefy evidence rather than speculative protocol changes.

## Primary change: long-URL QR defaults

The common verification URL supplied during testing is 74 UTF-8 bytes. On 40×20 mm stock with a 1.5 mm safe inset and ECC M, a Version-5 QR needs 45 total modules including the four-module quiet zone. The physically successful proof used 3 printer dots per module, producing a 135-dot (16.9 mm) QR.

v4.1.1 Quick Create targeted 132 dots, which forced that Version-5 payload down to 2 dots/module and triggered a blocking preflight error. v4.2.0 targets the full 136-dot safe-area square; integer module sizing then naturally renders the same payload at exactly **135 dots / 3 dots per module**.

## Additional refinements

- New QR elements use the active safe-area maximum by default.
- QR inspector gains **Maximize QR inside safe area**.
- Quick Create shows live QR byte/version/module geometry before rebuild.
- Long payload editing is easier on iPhone via a two-line textarea.
- QR + text gains 6 more dots of text width while preserving safe margins.
- Preflight removes redundant QR density warnings and duplicate text auto-fit warnings.

## What did not change

The B1 BLE transport, model verification, 240-byte bundle ceiling, 10–40 ms pacing, 15-second idle heartbeat, QR matrix generator, canonical 1-bit raster, RLE packetization, print-task sequencing, cancellation path, and Pixel-Faithful SVG conversion are unchanged from v4.1.1.
