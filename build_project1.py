import os
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Lenovo\Desktop\Projects\TCP-IP-Client-Server")
BASE_DIR.mkdir(parents=True, exist_ok=True)

PACKET_PY = '''"""
Custom binary packet framing and validation module.
Packet Format (Big-Endian):
    Magic Header  : 4 bytes (ASCII 'ABMS' for Abdullah Bin Masaud System)
    Payload Length: 4 bytes unsigned int (>I)
    CRC32 Checksum: 4 bytes unsigned int (>I)
    Payload       : N bytes UTF-8 / binary data
"""
import struct
import binascii

MAGIC = b"ABMS"
HEADER_FORMAT = ">4sII"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)


def encode_packet(payload: bytes, corrupt_checksum: bool = False) -> bytes:
    """Encodes a payload with magic header, length prefix, and CRC32 checksum."""
    length = len(payload)
    checksum = binascii.crc32(payload) & 0xFFFFFFFF
    if corrupt_checksum:
        checksum ^= 0xFFFFFFFF  # Invert bits to simulate bit-flip / transmission error

    header = struct.pack(HEADER_FORMAT, MAGIC, length, checksum)
    return header + payload


def decode_packet(raw_bytes: bytes) -> tuple[bytes, bool, str]:
    """
    Decodes a raw packet buffer.
    Returns: (payload, is_valid, error_message)
    """
    if len(raw_bytes) < HEADER_SIZE:
        return b"", False, f"Packet too short ({len(raw_bytes)} bytes, expected at least {HEADER_SIZE})"

    magic, length, expected_checksum = struct.unpack(HEADER_FORMAT, raw_bytes[:HEADER_SIZE])
    if magic != MAGIC:
        return b"", False, f"Magic mismatch: expected {MAGIC!r}, got {magic!r}"

    payload = raw_bytes[HEADER_SIZE:HEADER_SIZE + length]
    if len(payload) != length:
        return b"", False, f"Truncated payload: expected {length} bytes, got {len(payload)}"

    computed_checksum = binascii.crc32(payload) & 0xFFFFFFFF
    if computed_checksum != expected_checksum:
        return payload, False, f"CRC32 mismatch: expected 0x{expected_checksum:08X}, computed 0x{computed_checksum:08X}"

    return payload, True, "OK"
'''

SERVER_PY = '''"""
Multithreaded TCP Server with Packet Framing and Checksum Verification.
Listens on 127.0.0.1:9999 and processes incoming framed packets concurrently.
"""
import socket
import threading
import sys
from packet import decode_packet, encode_packet, HEADER_SIZE

HOST = "127.0.0.1"
PORT = 9999


def handle_client(conn: socket.socket, addr: tuple[str, int]) -> None:
    print(f"[+] Connection accepted from {addr[0]}:{addr[1]}")
    try:
        while True:
            # Step 1: Read fixed header
            header_bytes = b""
            while len(header_bytes) < HEADER_SIZE:
                chunk = conn.recv(HEADER_SIZE - len(header_bytes))
                if not chunk:
                    break
                header_bytes += chunk

            if not header_bytes:
                break

            if len(header_bytes) < HEADER_SIZE:
                print(f"[!] {addr} sent incomplete header. Closing.")
                break

            # Parse expected length from header
            import struct
            _, length, _ = struct.unpack(">4sII", header_bytes)

            # Step 2: Read exact payload length
            payload_bytes = b""
            while len(payload_bytes) < length:
                chunk = conn.recv(length - len(payload_bytes))
                if not chunk:
                    break
                payload_bytes += chunk

            full_packet = header_bytes + payload_bytes
            payload, is_valid, msg = decode_packet(full_packet)

            if is_valid:
                text = payload.decode("utf-8", errors="replace")
                print(f"[OK] {addr} -> Received ({len(payload)} bytes): {text}")
                response = encode_packet(b"ACK: Packet verified successfully.")
                conn.sendall(response)
            else:
                print(f"[ERROR] {addr} -> Checksum/Header validation failed: {msg}")
                response = encode_packet(f"NACK: {msg}".encode("utf-8"))
                conn.sendall(response)

    except ConnectionResetError:
        print(f"[-] Client {addr} disconnected abruptly.")
    except Exception as e:
        print(f"[!] Error handling client {addr}: {e}")
    finally:
        conn.close()
        print(f"[-] Closed connection from {addr[0]}:{addr[1]}")


def start_server(host: str = HOST, port: int = PORT) -> None:
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((host, port))
    server_sock.listen(10)
    print(f"============================================================")
    print(f"[*] TCP/IP Server running on {host}:{port}")
    print(f"[*] Multithreaded client handling ready. Press Ctrl+C to exit.")
    print(f"============================================================")

    try:
        while True:
            conn, addr = server_sock.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("\\n[*] Shutting down server.")
    finally:
        server_sock.close()


if __name__ == "__main__":
    start_server()
'''

CLIENT_PY = '''"""
TCP Client sending custom-framed packets with optional checksum corruption.
Usage:
    python client.py "Hello Server"
    python client.py "Corrupted packet test" --corrupt
"""
import socket
import argparse
from packet import encode_packet, decode_packet, HEADER_SIZE

HOST = "127.0.0.1"
PORT = 9999


def send_message(message: str, corrupt: bool = False, host: str = HOST, port: int = PORT) -> None:
    payload = message.encode("utf-8")
    packet_data = encode_packet(payload, corrupt_checksum=corrupt)

    print(f"[*] Connecting to {host}:{port}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    try:
        print(f"[*] Sending {len(payload)} bytes (Corrupt={corrupt})...")
        sock.sendall(packet_data)

        # Receive header
        header = b""
        while len(header) < HEADER_SIZE:
            chunk = sock.recv(HEADER_SIZE - len(header))
            if not chunk:
                break
            header += chunk

        import struct
        _, length, _ = struct.unpack(">4sII", header)

        payload_bytes = b""
        while len(payload_bytes) < length:
            chunk = sock.recv(length - len(payload_bytes))
            if not chunk:
                break
            payload_bytes += chunk

        resp_payload, valid, err = decode_packet(header + payload_bytes)
        print(f"[Server Response] (Valid={valid}): {resp_payload.decode('utf-8', errors='replace')}")

    finally:
        sock.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP/IP Client with Packet Framing")
    parser.add_argument("message", nargs="?", default="Telemetry packet ping test", help="Message text to send")
    parser.add_argument("--corrupt", action="store_true", help="Deliberately corrupt CRC32 to test error detection")
    args = parser.parse_args()

    send_message(args.message, corrupt=args.corrupt)
'''

LOAD_TEST_PY = '''"""
Concurrent Load Testing for Multithreaded TCP Server.
Spawns 10 client threads, each sending 5 packets, logging ACKs and NACKs.
"""
import socket
import threading
import time
from packet import encode_packet, decode_packet, HEADER_SIZE

HOST = "127.0.0.1"
PORT = 9999
NUM_THREADS = 10
MESSAGES_PER_THREAD = 5

results = {"ack": 0, "nack": 0, "error": 0}
lock = threading.Lock()


def worker(client_id: int) -> None:
    for i in range(MESSAGES_PER_THREAD):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5.0)
            sock.connect((HOST, PORT))

            # Introduce intentional corruption on 1 out of 5 packets to verify detection
            corrupt = (i % 5 == 3)
            msg = f"Worker-{client_id} Msg-{i}".encode("utf-8")
            packet = encode_packet(msg, corrupt_checksum=corrupt)
            sock.sendall(packet)

            header = b""
            while len(header) < HEADER_SIZE:
                chunk = sock.recv(HEADER_SIZE - len(header))
                if not chunk:
                    break
                header += chunk

            import struct
            _, length, _ = struct.unpack(">4sII", header)
            body = b""
            while len(body) < length:
                chunk = sock.recv(length - len(body))
                if not chunk:
                    break
                body += chunk

            payload, valid, _ = decode_packet(header + body)
            resp_text = payload.decode("utf-8", errors="replace")

            with lock:
                if "ACK" in resp_text:
                    results["ack"] += 1
                else:
                    results["nack"] += 1

            sock.close()
        except Exception as e:
            with lock:
                results["error"] += 1
        time.sleep(0.02)


if __name__ == "__main__":
    print(f"[*] Starting Load Test: {NUM_THREADS} threads x {MESSAGES_PER_THREAD} messages = {NUM_THREADS * MESSAGES_PER_THREAD} total...")
    start_time = time.time()
    threads = []
    for tid in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(tid,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    elapsed = time.time() - start_time
    total = results["ack"] + results["nack"] + results["error"]
    print("\\n" + "=" * 50)
    print("LOAD TEST SUMMARY RESULTS")
    print("=" * 50)
    print(f"Total Packets Sent : {total}")
    print(f"ACKs Received      : {results['ack']} (verified integrity)")
    print(f"NACKs Received     : {results['nack']} (detected simulated corruption)")
    print(f"Errors/Timeouts    : {results['error']}")
    print(f"Elapsed Time       : {elapsed:.2f} seconds")
    print(f"Throughput         : {total / elapsed:.1f} packets/sec")
    print("=" * 50)
'''

README_MD = '''# TCP/IP Client-Server Network Communication System

A low-level, multithreaded networking application demonstrating reliable packet transmission, custom framing, and CRC32 error detection over TCP/IP sockets.

## Architecture

```
+-------------------------------------------------------------+
|                      Packet Format                          |
+-------------------+-------------------+---------------------+
| Magic (4 bytes)   | Length (4 bytes)  | CRC32 (4 bytes)     |
| ASCII 'ABMS'      | Big-Endian uint32 | IEEE 802.3 Checksum |
+-------------------+-------------------+---------------------+
|                      Payload Data                           |
|                      (N bytes)                              |
+-------------------------------------------------------------+
```

## Features
- **Custom Framing:** Fixed 12-byte header prevents TCP stream fragmentation/sticky packet issues.
- **Integrity Validation:** 32-bit CRC checksum computed and verified on every transmission.
- **Multithreaded Server:** Handles concurrent connections seamlessly using thread-per-client model.
- **Error Injection Testing:** Client supports simulated bit corruption (`--corrupt`) to verify rejection logic.
- **Automated Load Testing:** Multi-threaded stress test simulating 10 concurrent clients.

## Quickstart

### Prerequisites
Only Python 3.8+ is required (uses Python standard library exclusively).

### 1. Start the Server
```bash
python server.py
```

### 2. Run a Client
```bash
# Valid transmission (server returns ACK)
python client.py "Sensors nominal"

# Corrupted transmission test (server detects and returns NACK)
python client.py "Transmission test" --corrupt
```

### 3. Run Concurrent Load Test
```bash
python load_test.py
```
'''

REQUIREMENTS_TXT = '''# This project uses the Python Standard Library exclusively:
# - socket
# - struct
# - binascii
# - threading
# - argparse
# No external pip dependencies required.
'''

files = {
    "packet.py": PACKET_PY,
    "server.py": SERVER_PY,
    "client.py": CLIENT_PY,
    "load_test.py": LOAD_TEST_PY,
    "README.md": README_MD,
    "requirements.txt": REQUIREMENTS_TXT,
}

for filename, content in files.items():
    file_path = BASE_DIR / filename
    file_path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Created {file_path}")

print("Project 1 (TCP-IP-Client-Server) built successfully!")
