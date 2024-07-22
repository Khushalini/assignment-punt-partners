
import time

class VoiceConversationSDK:
    def __init__(self):
        self.sttak = None
        self.llmak= None
        self.ttsak = None
        self.stte = "deepgram"
        self.ttse = "deepgram"  
        self.llme = "openai"
        self.sysp = "Please ask your question."

    def setup(self, sttak, ttsak, llmak):
        self.sttak = stt_api_key
        self.ttsak = tts_api_key
        self.llmak = llm_api_key
        print("SDK initialized successfully.")

sdk = VoiceConversationSDK()
sdk.setup("your deepgram stt_api_key", "your tts api_key", "your openai llm_api_key")


class VoiceConversationSDK:

    def stream_conversation(self, is ,os):
        CHUNK_SIZE = 1024
        audio_format = pyau.paInt16
        audio_rate = 16000  

        audio_input = pyau.PyAudio()
        stream_in = audio_input.open(format=audio_format, channels=1, rate=audio_rate,
                                     input=True, frames_per_buffer=CHUNK_SIZE)

        audio_output = pyau.PyAudio()
        stream_out = audio_output.open(format=audio_format, channels=1, rate=audio_rate,
                                       output=True)

         

    