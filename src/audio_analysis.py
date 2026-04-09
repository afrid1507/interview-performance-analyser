import whisper
import tempfile

model = whisper.load_model("base", device="cpu")

def transcribe_audio(audio_file):
    # create temporary file safely
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        tmp_path = tmp.name

    # transcribe
    result = model.transcribe(tmp_path)
    return result["text"]