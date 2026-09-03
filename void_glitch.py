#!/usr/bin/env python3
"""
void_glitch.py - VOID-GLITCH-PROTOCOL Engine
Double-SHA256 Toroidal Fold Execution.
"""
import hashlib
import json
import os

class VoidGlitchEngine:
    def __init__(self, manifest_path: str = "glitch_manifest.json"):
        self.manifest_path = manifest_path
        self.prime_clamps = (167, 761)
        self.state_hash = None

    def load_manifest(self) -> dict:
        if not os.path.exists(self.manifest_path):
            print(f"[-] Manifest {self.manifest_path} not found. Creating fallback.")
            return {"status": "fallback", "prime_clamps": list(self.prime_clamps)}
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def execute_toroidal_fold(self, payload: str) -> str:
        first_pass = hashlib.sha256(payload.encode('utf-8')).hexdigest()
        second_pass = hashlib.sha256(first_pass.encode('utf-8')).hexdigest()
        self.state_hash = second_pass
        return self.state_hash

    def run_protocol(self, payload: str = "Resonantia_Vinculum_Mundi"):
        manifest = self.load_manifest()
        print(f"[*] Manifest Loaded: {manifest.get('name', 'Void-Glitch-Core')}")
        fold_result = self.execute_toroidal_fold(payload)
        print(f"[+] Toroidal Fold Hash: {fold_result}")
        print(f"[+] Prime Clamps Locked: {self.prime_clamps}")
        return fold_result

if __name__ == "__main__":
    engine = VoidGlitchEngine()
    engine.run_protocol()
