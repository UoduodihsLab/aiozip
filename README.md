# aiozip

[](https://www.google.com/search?q=https://badge.fury.io/py/aiozip)
[](https://choosealicense.com/licenses/mit/)
[](https://www.google.com/search?q=https://pypi.org/project/aiozip)

**aiozip** is a Python library for high-performance, asynchronous archive handling, built with native `asyncio`.

The current phase focuses on providing a simple, unified API to decompress various common archive formats. Future versions will include compression capabilities.

## ✨ Key Features

  * **Truly Async**: Implements native asynchronous decompression for `.zip` files from the ground up, featuring non-blocking I/O throughout the process.
  * **Unified API**: A single, simple `aiozip.uncompress()` function handles multiple formats intelligently.
  * **Multi-Format Support**: Currently supports `.zip`, `.tar`, `.tar.gz`, and `.tar.bz2`.
  * **Lightweight**: Minimal dependencies, relying only on `aiofiles` for async file operations.
  * **Modern & Type-Hinted**: Built with modern Python 3.8+ features and includes full type hinting for better editor support and code quality.

## 🚀 Installation

```bash
pip install aiozip
```

## 💡 Quick Start

Using `aiozip` is straightforward. Here is a basic example of how to uncompress a `.zip` file.

```python
import asyncio
import aiozip

async def main():
    source_archive = "my_archive.zip"
    destination_dir = "./unzipped_files"

    try:
        print(f"Uncompressing '{source_archive}' to '{destination_dir}'...")
        # Assuming you have a file named my_archive.zip
        await aiozip.uncompress(source_archive, destination_dir)
        print("Uncompression complete!")

    except aiozip.AiozipError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # To run this example, create a dummy zip file first.
    # On macOS/Linux: echo "hello" > file.txt && zip my_archive.zip file.txt
    asyncio.run(main())
```

The same function works for other supported formats:

```python
# Uncompress a tarball
await aiozip.uncompress("my_archive.tar.gz", "./unzipped_tar_files")
```

## API Reference

### `await aiozip.uncompress(source_path, dest_path)`

Asynchronously uncompresses an archive file to a destination directory.

  * **`source_path` (str)**: Path to the source archive file.
  * **`dest_path` (str)**: Path to the destination directory. It will be created if it doesn't exist.

### Exceptions

The library raises specific exceptions, all inheriting from `aiozip.AiozipError`.

  * `aiozip.ArchiveNotFoundError`: Raised if the `source_path` does not exist.
  * `aiozip.UnsupportedFormatError`: Raised if the archive format is not supported.
  * `aiozip.CorruptArchiveError`: Raised if the archive file is corrupt or malformed.

## 🛣️ Roadmap

  * [ ] Implement truly asynchronous file **compression** capabilities.
  * [ ] Add support for more archive formats (e.g., `.7z`, subject to dependency availability).
  * [ ] Add support for handling password-protected archives.

## 🤝 Contributing

Contributions are welcome\! Feel free to submit a Pull Request or create an Issue for bugs, feature requests, or improvements.

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some amazing feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## 📄 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).