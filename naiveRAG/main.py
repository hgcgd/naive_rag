import os  # For file path handling
from dotenv import load_dotenv

# Load environment variables (optional, in case you have any)
load_dotenv()

from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

def process_pdf_file(input_file_path, result_type="markdown"):
    """Processes a PDF file using LlamaParse and returns the extracted text."""
    
    # Create a parser for the specific file type (PDF)
    parser = LlamaParse(result_type=result_type)
    
    # Map the file type to the parser
    file_extractor = {".pdf": parser}
    
    try:
        # Use SimpleDirectoryReader to read the directory containing the file
        # Ensure you pass a directory, not a single file
        # SimpleDirectoryReader is used for directories, not individual files
        reader = SimpleDirectoryReader(
            input_dir=os.path.dirname(input_file_path),  # Directory of the file
            file_extractor=file_extractor  # File type parser
        )

        # Load documents (it will process all files in the directory that match the extension)
        documents = reader.load_data()

        # Initialize an empty string to collect extracted text
        extracted_text = ""

        # Extract text from the loaded documents
        for doc in documents:
            extracted_text += doc.text

        return extracted_text

    except Exception as e:
        print(f"Error processing the PDF file: {e}")
        return ""

if __name__ == "__main__":
    # Specify the input PDF file path
    input_file_path = os.path.join(os.getcwd(), "fgit-cheat-sheet-education.pdf")  # Replace with actual file path

    # Check if the file exists before processing
    if not os.path.exists(input_file_path):
        print(f"File not found: {input_file_path}")
    else:
        # Process the file and get the extracted text
        extracted_text = process_pdf_file(input_file_path)

        # Write the extracted text to a Markdown file
        with open("output.md", "w") as file_handle:
            file_handle.write(extracted_text)

        print("Markdown file created successfully!")
