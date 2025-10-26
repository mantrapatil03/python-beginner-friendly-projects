import pyttsx3
from tkinter import Tk, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from contextlib import contextmanager

try:
    import docx
except ImportError:
    # Use a dummy Tk instance for the error message if docx is not installed
    root = Tk()
    root.withdraw()
    messagebox.showerror("Dependency Error", "python-docx library not found.\nPlease install it with: pip install python-docx")
    root.destroy()
    exit()

@contextmanager
def tkinter_root():
    """Context manager for a withdrawn tkinter root window."""
    root = Tk()
    root.withdraw()
    try:
        yield root
    finally:
        root.destroy()

def _initialize_engine() -> pyttsx3.Engine:
    """Initializes and configures the pyttsx3 engine."""
    engine = pyttsx3.init()
    rate = engine.getProperty("rate")
    engine.setProperty("rate", max(100, rate - 50))  # Slow down a bit more for clarity
    engine.setProperty("volume", 1.0)
    return engine

def docx_to_audio(docx_path: str):
    """Reads a .docx file and converts its text to audio."""
    try:
        document = docx.Document(docx_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Word document:\n{e}")
        return

    paragraphs = [p.text for p in document.paragraphs if p.text.strip()]
    if not paragraphs:
        messagebox.showwarning("No text", "No text found in the Word document.")
        return

    save_file = messagebox.askyesno("Save audio", "Save audio to a file instead of speaking?")
    engine = _initialize_engine()

    try:
        if save_file:
            out_path = asksaveasfilename(title="Save audio as", defaultextension=".wav",
                                         filetypes=[("WAV files", "*.wav"), ("All files", "*.*")])
            if not out_path:
                messagebox.showinfo("Cancelled", "Save cancelled.")
                return
            text_to_speak = "\n\n".join(paragraphs)
            engine.save_to_file(text_to_speak, out_path)
            engine.runAndWait()
            messagebox.showinfo("Done", f"Audio saved to:\n{out_path}")
        else:
            # speak paragraph by paragraph to keep responsiveness
            for i, paragraph_text in enumerate(paragraphs, start=1):
                if not paragraph_text.strip():
                    continue
                print(f"Speaking paragraph {i}/{len(paragraphs)}...")
                engine.say(paragraph_text)
                engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", f"Failed during speech processing:\n{e}")
    finally:
        engine.stop()

def main():
    """Main function to run the docx to audio converter."""
    with tkinter_root():
        docx_path = askopenfilename(title="Select Word Document", filetypes=[("Word Documents", "*.docx")])
        if not docx_path:
            print("No file selected. Exiting.")
            return

        docx_to_audio(docx_path)

if __name__ == "__main__":
    main()