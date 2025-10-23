#!/usr/bin/env python3
"""
Port Scanner - simple multi-threaded TCP port scanner
Usage: python3 port_scanner.py
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import socket
import argparse

def safe_service(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"

def scan_one(target, port, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        rc = s.connect_ex((target, port))
        return (target, port, rc == 0)
    except Exception:
        return (target, port, False)
    finally:
        s.close()

def main():
    parser = argparse.ArgumentParser(description="Simple multi-threaded TCP port scanner")
    parser.add_argument("target", nargs="?", default="192.168.1.1", help="target host or base network (e.g. 192.168.1.)")
    parser.add_argument("--network", action="store_true", help="treat target as base network and scan .1-.254")
    parser.add_argument("--start", type=int, default=1, help="start port")
    parser.add_argument("--end", type=int, default=100, help="end port")
    parser.add_argument("--timeout", type=float, default=0.8, help="socket timeout seconds")
    parser.add_argument("--workers", type=int, default=200, help="max threads")
    args = parser.parse_args()

    if args.network:
        base = args.target
        hosts = [f"{base}{i}" for i in range(1, 255)]
    else:
        hosts = [args.target]

    ports = range(args.start, args.end + 1)
    open_map = {}

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(scan_one, h, p, args.timeout): (h,p) for h in hosts for p in ports}
        for fut in as_completed(futures):
            host, port = futures[fut]
            try:
                _, _, is_open = fut.result()
            except Exception:
                is_open = False
            if is_open:
                svc = safe_service(port)
                open_map.setdefault(host, []).append((port, svc))

    if not open_map:
        print("No open ports found in the scanned range.")
    else:
        for host, lst in sorted(open_map.items()):
            print(f"\n[+] {host} -> {len(lst)} open:")
            for port, svc in sorted(lst):
                print(f"    - Port {port} open ({svc})")

if __name__ == "__main__":
    main()
