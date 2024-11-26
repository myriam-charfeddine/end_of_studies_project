import torch
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
from transformers import  pipeline
import librosa
from transformers import ( Wav2Vec2ForCTC, Wav2Vec2Processor)

class ASRModel:
    def __init__(self, torch_dtype=torch.float32, device=None, language='En'):
        try:
            self.language = language
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch_dtype

            #...........ENGLISH MODEL.................................. 
            self.eng_model_id = r".\Distil-whisper"
            self.eng_processor = AutoProcessor.from_pretrained(self.eng_model_id)
            self.eng_model = AutoModelForSpeechSeq2Seq.from_pretrained(self.eng_model_id, torch_dtype=self.torch_dtype)
            self.eng_model.to(self.device)
            self.eng_transcriber = pipeline(
                "automatic-speech-recognition",
                model=self.eng_model,
                tokenizer=self.eng_processor.tokenizer,
                feature_extractor=self.eng_processor.feature_extractor,
                #max_new_tokens=128,
                torch_dtype=self.torch_dtype,
                device=self.device,
                )
            
            #...........TUNISIEN MODEL..................................
            self.tun_model = Wav2Vec2ForCTC.from_pretrained(r".\tun_final_final\model")
            self.tun_processor = Wav2Vec2Processor.from_pretrained(r".\tun_final_final\processor")
            self.tun_model.to(self.device)
          
        except Exception as e:
            print(f"Error loading ASR model: {e}")

    def transcribe_audio(self, audio_file):
        try:
            if self.language == 'En':
                transcription = self.eng_transcriber(audio_file)['text']

            else:
                speech, _ = librosa.load(audio_file, sr=16000)
                features = self.tun_processor(speech, sampling_rate=16000, return_tensors="pt")
                input_values = features.input_values
                input_values = input_values.to(self.device)
                with torch.no_grad():
                    logits = self.tun_model(input_values).logits
                    pred_ids = torch.argmax(logits, dim=-1) 
                    pred_text = self.tun_processor.batch_decode(pred_ids)[0]
                transcription = pred_text

            return transcription
        
        except Exception as e:
            # print(f"Error transcribing audio: {e}")
            return None
        
    def get_language(self):
        return self.language
    
    def set_language(self, lang):
        self.language = lang
    
        print(self.language)
       
    

