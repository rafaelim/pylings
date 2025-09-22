import os
import tempfile
import unittest

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.filepath = self.temp_file.name
        self.temp_file.close()

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

    def test_file_write_string(self):
        content = 'Hello, World!'
        with open(self.filepath, "w") as f:
            f.write(content)

        with open(self.filepath, "r") as f:
            read_content = f.read()
            self.assertEqual(read_content, content)

    def test_file_append_string(self):
        first_line = 'First line\n'
        second_line = 'Second line'
        with open(self.filepath, "w") as f:
            f.write(first_line)

        with open(self.filepath, "a") as f:
            f.write(second_line)

        with open(self.filepath, "r") as f:
            read_content = f.read()
            self.assertEqual(read_content, first_line + second_line)

    def test_file_write_empty_string(self):
        content = ""
        with open(self.filepath, "w") as f:
            f.write(content)

        with open(self.filepath, "r") as f:
            read_content = f.read()
            self.assertEqual(read_content, "")

    def test_file_write_multiple_row_strings(self):
        content = """
        > Row 1
        > Row 2
        > Row 3
        """
        with open(self.filepath, "w") as f:
            f.write(content)

        with open(self.filepath, "r") as f:
            read_content = f.read()
            self.assertEqual(read_content, content)
    
    def test_file_write_long_string(self):
        content = "a" * 1_000
        with open(self.filepath, "w") as f:
            f.write(content)

        with open(self.filepath, "r") as f:
            read_content = f.read()
            self.assertEqual(read_content, content)

    def test_file_read_line_by_line(self):
        content = "First line\nSecond line\nThird line"
        with open(self.filepath, "w") as f:
            f.write(content)

        with open(self.filepath, "r") as f:
            self.assertEqual(f.readline(), "First line\n")
            self.assertEqual(f.readline(), "Second line\n")
            self.assertEqual(f.readline(), "Third line")

        with open(self.filepath, "r") as f:
            lines = f.readlines()
            self.assertEqual(lines, ["First line\n", "Second line\n", "Third line"])

    def test_file_read_write_simultaneously(self):
        with open(self.filepath, "w") as f:
            f.write("Initial content")
        
        with open(self.filepath, "r+") as f:
            self.assertEqual(f.read(), "Initial content")
            f.seek(0)
            f.write("New content")
            f.truncate()
        
        with open(self.filepath, "r") as f:
            self.assertEqual(f.read(), "New content")

    def test_read_nonexistent_file(self):
        nonexistent_filepath = "non_existent_file.txt"
        self.assertFalse(os.path.exists(nonexistent_filepath))
        with self.assertRaises(FileNotFoundError):
            with open(nonexistent_filepath, "r") as f:
                f.read()


if __name__ == '__main__':
    unittest.main()
