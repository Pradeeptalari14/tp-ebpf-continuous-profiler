[![Ecosystem](https://img.shields.io/badge/Portfolio%20Ecosystem-341%20Studios-6366f1.svg)](https://pradeeptalari.me/projects/)
[![Architecture DAG](https://img.shields.io/badge/Architecture-DAG%20%26%20Course-10b981.svg)](https://pradeeptalari.me/tools/repo-learning/)

# Continuous eBPF Kernel Profiler & FlameGraph Studio

[![CI SRE Validation](https://github.com/Pradeeptalari14/tp-ebpf-continuous-profiler/actions/workflows/sre-validation.yml/badge.svg)](https://github.com/Pradeeptalari14/tp-ebpf-continuous-profiler/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Linux eBPF CO-RE](https://img.shields.io/badge/Platform-Linux%20Kernel%206.x-emerald.svg)](https://talaripradeep.info)

Production-grade implementation of **Zero-Overhead Continuous eBPF Profiling** and dynamic WebGL FlameGraph aggregation with OpenTelemetry Profiling support.

![eBPF Architecture Flow](docs/ebpf_flamegraph_flow.png)

## Key Technical Highlights
- **Sub-1% CPU Overhead:** Profiles system-wide stack traces at 99Hz directly via BPF ring buffers without thread interruption or process restarts.
- **DWARF & Frame Pointer Unwinding:** Dual stack unwinding mode resolving kernel and userland symbol tables on-the-fly.
- **Off-CPU Lock Tracking:** Measures sleep and scheduler contention events to pinpoint thread lock starvation.
- **OpenTelemetry Profiler Sink:** Emits OTLP/HTTP profiling payloads to Grafana Pyroscope and OpenTelemetry collectors.

## Quickstart
```bash
git clone https://github.com/Pradeeptalari14/tp-ebpf-continuous-profiler.git
cd tp-ebpf-continuous-profiler
bash scripts/validate.sh
```

---
*Synchronized with [Continuous eBPF Kernel Profiler & FlameGraph Studio Studio](https://pradeeptalari.me/tools/ebpf-continuous-profiler/) & [Repository Learning DAG](https://pradeeptalari.me/tools/repo-learning/) — [Talari Pradeep Portfolio](https://pradeeptalari.me)*
