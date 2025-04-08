import pyttsx3
import docx
import re
import argparse
import PyPDF2

def remove_brackets_text(text):
    # Remove text within both parentheses and square brackets
    text = re.sub(r'\[[^\]]*\]', '', text)  # Remove text inside square brackets
    text = re.sub(r'\([^)]*\)', '', text)  # Remove text inside parentheses
    return text

def read_docx_out_loud(file_path, rate=150, voice="male", start_paragraph=1):
    engine = pyttsx3.init()

    # Set the rate (speed)
    engine.setProperty('rate', rate)

    # Get available voices
    voices = engine.getProperty('voices')

    # Select the voice: either male or female 
    if voice == "female":
        engine.setProperty('voice', voices[0].id)  # Female voice 
    elif voice == "male":
        engine.setProperty('voice', voices[1].id)  # Male voice 
    
    doc = docx.Document(file_path)

    # Convert start_paragraph to 0-based index
    start_paragraph = start_paragraph - 1

    # Start reading from the specified paragraph (start_paragraph is now 0-indexed)
    for para_index, para in enumerate(doc.paragraphs[start_paragraph:], start=start_paragraph):
        cleaned = remove_brackets_text(para.text)
        if cleaned.strip():
            print(f"Paragraph {para_index + 1}: {cleaned.strip()}")
            engine.say(cleaned.strip())
            engine.runAndWait()  # Ensure it speaks each line immediately

def read_pdf_out_loud(file_path, rate=150, voice="male", start_page=1):
    engine = pyttsx3.init()

    # Set the rate (speed)
    engine.setProperty('rate', rate)

    # Get available voices
    voices = engine.getProperty('voices')

    # Select the voice: either male or female (or change as needed)
    if voice == "female":
        engine.setProperty('voice', voices[0].id)  # Female voice 
    elif voice == "male":
        engine.setProperty('voice', voices[1].id)  # Male voice 

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Convert start_page to 0-based index
        start_page = start_page - 1

        # Start reading from the specified page (start_page is now 0-indexed)
        for page_index, page in enumerate(reader.pages[start_page:], start=start_page):
            text = page.extract_text()
            if text:
                cleaned = remove_brackets_text(text)
                if cleaned.strip():
                    print(f"Page {page_index + 1}: {cleaned.strip()}")
                    engine.say(cleaned.strip())
                    engine.runAndWait()  # Ensure it speaks each page immediately

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Read a .docx or .pdf file aloud, skipping text in parentheses and square brackets.')
    parser.add_argument('file_path', type=str, help='The path to the file (.docx or .pdf)')
    parser.add_argument('--rate', type=int, default=150, help='Rate (speed) of speech (default: 150)')
    parser.add_argument('--voice', choices=['male', 'female'], default='male', help='Voice type (default: male)')
    parser.add_argument('--start', type=int, default=1, help='Starting paragraph (for .docx) or page (for .pdf), default is 1')

    args = parser.parse_args()

    # Check file type and call appropriate function
    if args.file_path.endswith('.docx'):
        read_docx_out_loud(args.file_path, rate=args.rate, voice=args.voice, start_paragraph=args.start)
    elif args.file_path.endswith('.pdf'):
        read_pdf_out_loud(args.file_path, rate=args.rate, voice=args.voice, start_page=args.start)
    else:
        print("Unsupported file type. Please provide a .docx or .pdf file.")
