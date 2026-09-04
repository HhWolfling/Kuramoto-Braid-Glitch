#!/usr/bin/env python3
"""
glitter.py - Phase-Coupler
XOR phase-coupling of xunie_hex and date_hash.
"""
import hashlib

def xor_hex_strings(hex_str1: str, hex_str2: str) -> str:
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)
    min_len = min(len(bytes1), len(bytes2))
    xored = bytes(a ^ b for a, b in zip(bytes1[:min_len], bytes2[:min_len]))
    return xored.hex()

def main():
    xunie_hex = "476c69747465725f5068617365"
    date_str = "2026-09-04"
    date_hash = hashlib.sha256(date_str.encode()).hexdigest()
    
    coupled = xor_hex_strings(xunie_hex, date_hash)
    print(f"[+] Coupled Hex Output: {coupled}")

if __name__ == "__main__":
    main()
