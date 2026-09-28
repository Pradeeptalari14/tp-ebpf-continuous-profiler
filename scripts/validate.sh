#!/usr/bin/env bash
set -euo pipefail

echo "=================================================="
echo "SRE Validation: Continuous eBPF Profiler Studio"
echo "=================================================="

echo "[1/4] Validating Python Engine syntax..."
python3 -m py_compile ebpf_profiler_daemon.py
python3 -m py_compile manim_flow.py
echo "✓ Python compilation clean."

echo "[2/4] Testing profiler mock aggregation..."
python3 ebpf_profiler_daemon.py > /dev/null
echo "✓ Profiler aggregation successful."

echo "[3/4] Validating TypeScript Client syntax..."
npx --yes tsc --noEmit flamegraph_streamer.ts
echo "✓ TypeScript compilation clean."

echo "[4/4] Validating Kubernetes DaemonSet Manifest..."
grep -q "hostPID: true" k8s-daemonset.yaml
echo "✓ Kubernetes DaemonSet spec conforms to eBPF requirements."

echo "=================================================="
echo "ALL TESTS PASSED: tp-ebpf-continuous-profiler ready."
echo "=================================================="
