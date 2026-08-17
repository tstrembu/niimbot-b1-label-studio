#!/usr/bin/env python3
import base64, gzip, hashlib, json, pathlib, sys

BASE_SHA = "b0e454f0d5720ddc24c5ce6c3ec616ad20a1cada854eb7aa40918abea5ccdb52"
OUT_SHA = "8360ee3661da495538eec598908e470ecfb7aa31b76b3b7d15bb8a9530c207bb"
OUT_BYTES = 181130

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()

def main():
    if len(sys.argv) != 4:
        raise SystemExit("usage: apply_v420.py BASE_HTML PATCH_B64 OUTPUT_HTML")
    base_path, patch_path, out_path = map(pathlib.Path, sys.argv[1:])
    base = base_path.read_bytes()
    got = sha256_bytes(base)
    if got != BASE_SHA:
        raise SystemExit(f"base SHA mismatch: {got}")
    payload = gzip.decompress(base64.b64decode(patch_path.read_text().strip()))
    changes = json.loads(payload.decode("utf-8"))
    text = base.decode("utf-8")
    had_final_nl = text.endswith("\n")
    lines = text.splitlines()
    for key in sorted(changes, key=lambda x:int(x)):
        line_no = int(key)
        if line_no < 1 or line_no > len(lines):
            raise SystemExit(f"patch line out of range: {line_no}")
        lines[line_no - 1] = changes[key]
    out = "\n".join(lines) + ("\n" if had_final_nl else "")
    data = out.encode("utf-8")
    out_hash = sha256_bytes(data)
    if out_hash != OUT_SHA:
        raise SystemExit(f"v4.2.0 SHA mismatch: {out_hash}")
    if len(data) != OUT_BYTES:
        raise SystemExit(f"v4.2.0 size mismatch: {len(data)}")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    print(f"v4.2.0 verified: {out_hash} · {len(data)} bytes")

if __name__ == "__main__":
    main()
