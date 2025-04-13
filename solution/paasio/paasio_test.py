import unittest
import io
import socket
from unittest.mock import patch, MagicMock
from paasio import MeteredFile, MeteredSocket


class MeteredFileTester(unittest.TestCase):
    """Test cases for the MeteredFile class."""
    
    def test_init_with_default_bytesio(self):
        """Test initialization with no arguments."""
        file = MeteredFile()
        self.assertEqual(0, file.read_bytes)
        self.assertEqual(0, file.read_ops)
        self.assertEqual(0, file.write_bytes)
        self.assertEqual(0, file.write_ops)
        
    def test_init_with_custom_file(self):
        """Test initialization with a custom file object."""
        mock_file = io.BytesIO(b"test data")
        file = MeteredFile(mock_file)
        self.assertEqual(0, file.read_bytes)
        self.assertEqual(0, file.read_ops)
        
    def test_read_tracks_operations_and_bytes(self):
        """Test that read operations and bytes are tracked correctly."""
        file = MeteredFile(io.BytesIO(b"test data"))
        data = file.read(4)
        self.assertEqual(b"test", data)
        self.assertEqual(4, file.read_bytes)
        self.assertEqual(1, file.read_ops)
        
        data = file.read()
        self.assertEqual(b" data", data)
        self.assertEqual(9, file.read_bytes)
        self.assertEqual(2, file.read_ops)
        
    def test_write_tracks_operations_and_bytes(self):
        """Test that write operations and bytes are tracked correctly."""
        file = MeteredFile(io.BytesIO())
        bytes_written = file.write(b"hello")
        self.assertEqual(5, bytes_written)
        self.assertEqual(5, file.write_bytes)
        self.assertEqual(1, file.write_ops)
        
        bytes_written = file.write(b" world")
        self.assertEqual(6, bytes_written)
        self.assertEqual(11, file.write_bytes)
        self.assertEqual(2, file.write_ops)
        
    def test_context_manager(self):
        """Test that the file works as a context manager."""
        with MeteredFile(io.BytesIO(b"test data")) as file:
            data = file.read()
            self.assertEqual(b"test data", data)
            self.assertEqual(9, file.read_bytes)
            self.assertEqual(1, file.read_ops)
            
    def test_iteration(self):
        """Test that the file can be iterated over."""
        content = b"line1\nline2\nline3"
        file = MeteredFile(io.BytesIO(content))
        lines = []
        for line in file:
            lines.append(line)
            
        self.assertEqual([b"line1\n", b"line2\n", b"line3"], lines)
        self.assertEqual(len(content), file.read_bytes)
        self.assertEqual(3, file.read_ops)
        
    def test_readline(self):
        """Test that readline works and tracks operations."""
        content = b"line1\nline2\nline3"
        file = MeteredFile(io.BytesIO(content))
        
        line = file.readline()
        self.assertEqual(b"line1\n", line)
        self.assertEqual(6, file.read_bytes)
        self.assertEqual(1, file.read_ops)
        
        line = file.readline()
        self.assertEqual(b"line2\n", line)
        self.assertEqual(12, file.read_bytes)
        self.assertEqual(2, file.read_ops)


class MeteredSocketTester(unittest.TestCase):
    """Test cases for the MeteredSocket class."""
    
    def setUp(self):
        """Set up a mock socket for testing."""
        self.mock_socket = MagicMock()
        self.mock_socket.recv.return_value = b"test data"
        self.mock_socket.send.return_value = 9
        
    def test_init(self):
        """Test initialization."""
        socket = MeteredSocket(self.mock_socket)
        self.assertEqual(0, socket.recv_bytes)
        self.assertEqual(0, socket.recv_ops)
        self.assertEqual(0, socket.send_bytes)
        self.assertEqual(0, socket.send_ops)
        
    def test_recv_tracks_operations_and_bytes(self):
        """Test that recv operations and bytes are tracked correctly."""
        socket = MeteredSocket(self.mock_socket)
        data = socket.recv(1024)
        self.assertEqual(b"test data", data)
        self.assertEqual(9, socket.recv_bytes)
        self.assertEqual(1, socket.recv_ops)
        
        data = socket.recv(1024)
        self.assertEqual(b"test data", data)
        self.assertEqual(18, socket.recv_bytes)
        self.assertEqual(2, socket.recv_ops)
        
    def test_send_tracks_operations_and_bytes(self):
        """Test that send operations and bytes are tracked correctly."""
        socket = MeteredSocket(self.mock_socket)
        bytes_sent = socket.send(b"hello")
        self.assertEqual(9, bytes_sent)  # Using mocked return value
        self.assertEqual(9, socket.send_bytes)
        self.assertEqual(1, socket.send_ops)
        
        bytes_sent = socket.send(b"world")
        self.assertEqual(9, bytes_sent)  # Using mocked return value
        self.assertEqual(18, socket.send_bytes)
        self.assertEqual(2, socket.send_ops)
        
    def test_context_manager(self):
        """Test that the socket works as a context manager."""
        self.mock_socket.__enter__.return_value = self.mock_socket
        self.mock_socket.__exit__.return_value = None
        
        with MeteredSocket(self.mock_socket) as socket:
            data = socket.recv(1024)
            self.assertEqual(b"test data", data)
            self.assertEqual(9, socket.recv_bytes)
            self.assertEqual(1, socket.recv_ops)
        
        self.mock_socket.__exit__.assert_called_once()
        
    def test_flags_passed_to_underlying_socket(self):
        """Test that flags are passed to the underlying socket."""
        socket = MeteredSocket(self.mock_socket)
        socket.recv(1024, 42)
        self.mock_socket.recv.assert_called_with(1024, 42)
        
        socket.send(b"data", 33)
        self.mock_socket.send.assert_called_with(b"data", 33)
        
    def test_invalid_flags_raise_type_error(self):
        """Test that invalid flags raise a TypeError."""
        socket = MeteredSocket(self.mock_socket)
        
        with self.assertRaises(TypeError):
            socket.recv(1024, "not an int")
            
        with self.assertRaises(TypeError):
            socket.send(b"data", "not an int")


if __name__ == '__main__':
    unittest.main()
