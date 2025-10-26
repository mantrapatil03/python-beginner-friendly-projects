# Document to Audio Converter

A simple Python utility to convert text from Microsoft Word (`.docx`) documents into spoken audio. You can either listen to the audio directly or save it as a `.wav` file.

This script uses a simple, dialog-based interface for file selection and options.

## Features

-   Reads text content from `.docx` files.
-   Converts the extracted text into speech.
-   **Option 1:** Speak the text aloud, paragraph by paragraph.
-   **Option 2:** Save the entire text as a single `.wav` audio file.
-   Handles missing dependencies and file-opening errors gracefully.

## Requirements

-   Python 3.x
-   The following Python libraries:
    -   `pyttsx3`
    -   `python-docx`
    -   `pypiwin32` (often required by `pyttsx3` on Windows)

## Installation

1.  Clone this repository or download the `Pdftoaudio.py` script.

2.  Install the required libraries using pip:

    ```bash
    pip install pyttsx3 python-docx pypiwin32
    ```

## How to Use

1.  Run the script from your terminal:

    ```bash
    python Pdftoaudio.py
    ```

2.  A file dialog will open. Select the `.docx` document you want to convert.

3.  A dialog box will ask if you want to save the audio to a file.
    -   Click **"Yes"** to open a "Save As" dialog and save the output as a `.wav` file.
    -   Click **"No"** to have the script speak the document's text aloud directly.

4.  Follow the on-screen prompts. Status messages will be printed to the console.

## Recent Code Improvements

The script was recently refactored to improve its quality, robustness, and maintainability. Key improvements include:

-   **Dependency Management:** Imports are now organized at the top of the file. A startup check was added to ensure the `python-docx` library is installed, providing a user-friendly error message if it's missing.
-   **Robustness:**
    -   The `tkinter` root window is now managed with a `contextmanager`, ensuring it is always properly destroyed.
    -   A `try...finally` block was added around the text-to-speech engine logic to guarantee that `engine.stop()` is called, preventing the engine from hanging in case of an error.
-   **Code Structure & Readability:**
    -   The `pyttsx3` engine setup was moved into its own helper function (`_initialize_engine`) to keep the main logic clean.
    -   Type hints and docstrings were added to all functions, making the code self-documenting and easier to understand.

## Future Roadmap

This project is a great starting point, and there are several exciting features planned for the future to make it more powerful and user-friendly.

-   **Support for More File Formats:**
    -   Add support for reading text from **PDF files** (`.pdf`).
    -   Add support for plain text files (`.txt`).

-   **Full Graphical User Interface (GUI):**
    -   Move away from simple dialog boxes to a complete GUI built with a framework like `tkinter` or `PyQt`.
    -   The GUI would include features like a progress bar, play/pause/stop controls for live playback, and status displays.

-   **Enhanced Audio Controls:**
    -   Allow the user to select from available system voices.
    -   Provide a slider or input box to adjust the speech rate and volume directly from the UI.

-   **Cross-Platform Compatibility:**
    -   Test and ensure the script works seamlessly on macOS and Linux. This may involve handling different text-to-speech engine backends.

-   **Application Packaging:**
    -   Package the application as a standalone executable (e.g., using `PyInstaller`) so that users can run it without needing to have Python or any libraries installed.

## Contributing

Contributions are welcome! If you'd like to help with any of the features on the roadmap or fix a bug, please feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.