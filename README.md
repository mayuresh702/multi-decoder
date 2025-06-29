# 🔐 Multi Decoder

A Python 3 script to decode encoded strings using multiple formats — useful for CTFs, pentesting, reverse engineering, or general analysis.

**Supports decoding from:**

* Base64
* Base32
* Base58
* Base62 (bash62 alphabet)
* Base91
* Hexadecimal
* Binary
* Ascii85 (Adobe & raw)

---

## 📦 Installation

### 1. Clone this repository:

```bash
git clone https://github.com/mayuresh702/multi_decoder.git
cd multi_decoder
```

### 2. Run with Python 3:

```bash
python3 multi_decoder.py
```

> ✅ No dependencies needed — 100% standard Python libraries.

---

## 🚀 Usage

Just enter an encoded string when prompted:

```bash
$ python3 multi_decoder.py

Enter encoded string: AGtWjiJstl5mcfo
```

You’ll see decoded results (or failures) for all supported formats:

```
[✓] Base64:
kVï"l¯^fq¶

[✓] Base62 (bash62):
iammayuresh

[x] Base32 failed.
...
```

---

## 🧐 Why Use This?

This script tries to decode any given string using multiple encoding schemes and shows all results — making it perfect for:

* CTFs (Capture The Flag)
* OSINT investigations
* Pentesting tools
* Malware reversing
* Debugging encoded strings

---

## 🛠 Supported Formats

| Format  | Notes                         |
| ------- | ----------------------------- |
| Base64  | Auto-padded if needed         |
| Base32  | Auto-padded                   |
| Base58  | Bitcoin-style (no 0OIl)       |
| Base62  | Bash62 variant (`0-9A-Za-z`)  |
| Base91  | High-density custom encoding  |
| Hex     | Standard hex strings          |
| Binary  | Only raw binary strings (0/1) |
| Ascii85 | Adobe and raw modes supported |

---
