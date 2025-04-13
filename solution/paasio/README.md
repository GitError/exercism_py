# Paasio

A library for tracking network and file I/O operations in Python.

## Description

This library provides two classes that help track I/O operations:

1. `MeteredFile` - Extends `io.BufferedRandom` to track read/write operations on files
2. `MeteredSocket` - A wrapper around socket objects to track send/receive operations

These classes are useful for monitoring and reporting I/O usage, which can be essential for billing in PaaS (Platform as a Service) applications, performance monitoring, and debugging.

## Usage

### MeteredFile

```python
import io
from paasio import MeteredFile

# Create a MeteredFile with a BytesIO object
with MeteredFile(io.BytesIO(b"example data")) as file:
    data = file.read(7)  # Read 7 bytes
    print(data)  # b"example"
    
    print(f"Bytes read: {file.read_bytes}")  # Bytes read: 7
    print(f"Read operations: {file.read_ops}")  # Read operations: 1
    
    bytes_written = file.write(b" modified")
    print(f"Bytes written: {file.write_bytes}")  # Bytes written: 9
    print(f"Write operations: {file.write_ops}")  # Write operations: 1
```

### MeteredSocket

```python
import socket
from paasio import MeteredSocket

# Create a real socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))

# Wrap it with a MeteredSocket
with MeteredSocket(sock) as metered_sock:
    metered_sock.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    data = metered_sock.recv(4096)
    
    print(f"Bytes sent: {metered_sock.send_bytes}")
    print(f"Send operations: {metered_sock.send_ops}")
    print(f"Bytes received: {metered_sock.recv_bytes}")
    print(f"Receive operations: {metered_sock.recv_ops}")
```

## Features

- Track the number of bytes read/written or sent/received
- Track the number of read/write or send/receive operations
- Works with context managers (with statements)
- Preserves original file and socket functionality

## Implementation Details

### MeteredFile

- Subclasses `io.BufferedRandom`
- Overrides `read()`, `readline()`, and `write()` methods to track operations
- Provides `read_bytes`, `read_ops`, `write_bytes`, and `write_ops` properties

### MeteredSocket

- Uses delegation pattern to wrap a socket object
- Implements `recv()` and `send()` methods that track operations
- Provides `recv_bytes`, `recv_ops`, `send_bytes`, and `send_ops` properties

## Requirements

- Python 3.6 or later
- No external dependencies

## Running Tests

```bash
python -m unittest paasio_test.py
```
