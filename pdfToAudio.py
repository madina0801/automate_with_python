import PyPDF2
from gtts import gTTS

def pdf_to_text(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_audio(text, output_file='pdfToAudio.mp3', lang='en', speed=1.5):
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    print(f"Audio saved as '{output_file}'")

if __name__ == "__main__":
    pdf_file = 'story.pdf'
    text = pdf_to_text(pdf_file)
    text_to_audio(text)

