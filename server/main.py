import wave
from scripts import scripts
import speech_recognition as sr
from state import State
from langgraph.graph import StateGraph, END
        
# ...............Main pipeline class........................

class LiveSpeechToText:
    def __init__(self, asr_model,  graph_nodes):
        self.asr_model = asr_model
        self.running = False
        self.transcription = ""
        self.prediction = ""
        self.recorder = sr.Recognizer()
        self.source = sr.Microphone(sample_rate=44100)
        self.pipeline_feedback = ""
 
        # ............Build the graph for script prediction + execution
        self.graph_nodes = graph_nodes
        graph_builder = StateGraph(State)

        #Adding nodes to the graph
        graph_builder.add_node("pts_related", self.graph_nodes.pts_related)
        graph_builder.add_node("script_predicter_executer", self.graph_nodes.script_predicter_executer)

        #Adding edges to the graph
        graph_builder.add_edge("pts_related", "script_predicter_executer")
        graph_builder.add_edge("script_predicter_executer", END)
        graph_builder.set_entry_point("pts_related")
        
        #Compile graph
        self.workflow = graph_builder.compile()
    
    def get_data(self):
        return self.transcription, self.prediction, self.pipeline_feedback
    
    def record_with_time_out(self):
        try:
          
          self.pipeline_feedback = ""

          with self.source:
            audio = self.recorder.listen(self.source, timeout=4, phrase_time_limit=7)
            # audio = self.recorder.record(self.source, duration=8)
            audio_file="temp_audio_2"+".wav"
            with wave.open(audio_file, 'wb') as wf:
                            wf.setnchannels(1)  # mono
                            wf.setsampwidth(2)   # 16-bit
                            wf.setframerate(44100)
                            wf.writeframes(audio.get_wav_data())
            self.transcription = self.asr_model.transcribe_audio(audio_file)
    
        except Exception as e:
            self.pipeline_feedback = "Error during transcribing audio!"
            print(f"Error duriing transcription {e}")

        try:
            self.prediction = self.workflow.invoke({"transcription": self.transcription})["predicted_script"]

            # .................
            
            #Handle None prediction
            if self.prediction == 'None' or self.prediction== "" :
               self.pipeline_feedback = "Command not recognized. Please repeat your desired order again!"

        except Exception as e:
            print(f"Error during script prediction: {e}")
            self.pipeline_feedback = "Failed to predcit your desired order!"

        # ...
   

