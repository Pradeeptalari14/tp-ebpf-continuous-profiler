/**
 * WebGL / SVG Differential FlameGraph Streamer Client
 */

export interface FlameNode {
  name: string;
  value: number;
  children?: FlameNode[];
}

export class FlamegraphStreamer {
  private ws: WebSocket | null = null;
  private endpoint: string;

  constructor(endpoint: string = "ws://localhost:9102/profiles/stream") {
    this.endpoint = endpoint;
  }

  public connect(onFrame: (data: FlameNode) => void): void {
    console.log(`Connecting to eBPF continuous profile stream at ${this.endpoint}...`);
    // Simulated stream packet
    setTimeout(() => {
      onFrame({
        name: "all",
        value: 1500,
        children: [
          { name: "kernel_space", value: 650 },
          { name: "user_app", value: 850 }
        ]
      });
    }, 100);
  }
}
