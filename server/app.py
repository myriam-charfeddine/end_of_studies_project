from flask import Flask, render_template, jsonify, request
from main import LiveSpeechToText
from asr_pipeline import ASRModel
from selenium import webdriver
from scripts import FirefoxScriptAutomation
import os
from langgraph.graph import StateGraph, END
from state import State
from scripts import scripts
from gemini_prompt_engineer import GeminiPromptEngineer
from typing import Dict, TypedDict
from llama_prompt_engineer import LLaMAPromptEngineer


from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# ..............Graph.........................
# ..............Graph Nodes...................

class graphNodes:
    def __init__(self, scripts, prompt_engineer):
            self.scripts = scripts
            self.prompt_engineer = prompt_engineer
            

    def pts_related(self, state: State):
            # to_pts = state.get("to_pts")
            # print("to_pts: ", to_pts)
            print("Your order is going to be executed in PTS!")

    def script_predicter_executer(self, state: State) -> Dict[str, str]:
            
            transcription = state.get("transcription")
            predicted_script = self.prompt_engineer.predict_endpoint_details(self.scripts, transcription)
            try:
                exec(predicted_script)
            except Exception as e:
                print("error executing script: ",e)
            
            return {"predicted_script": predicted_script}
    
prompt_engineer = GeminiPromptEngineer()  # !!!!!!!  To use llama3 call LLaMAPromptEngineer()
graph_nodes = graphNodes(scripts, prompt_engineer)
asr_model = ASRModel()
live = LiveSpeechToText(asr_model, graph_nodes)

# PTS Scripts 
firefox_auto_script = FirefoxScriptAutomation()
create_new_ticket = firefox_auto_script.create_ticket_script
add_new_comment = firefox_auto_script.add_comment_script
update_ticket = firefox_auto_script.update_ticket
add_attachment = firefox_auto_script.add_attachment
set_answer = firefox_auto_script.set_answer
set_ticket_as_answered = firefox_auto_script.set_ticket_as_answered
discard_changes = firefox_auto_script.discard_changes
start_chat = firefox_auto_script.start_chat
write_in_chat = firefox_auto_script.write_in_chat
send_message = firefox_auto_script.send_message
close_chat = firefox_auto_script.close_chat
send_file_in_chat = firefox_auto_script.send_file_in_chat
send_emoji_in_chat = firefox_auto_script.send_emoji_in_chat
set_estimated_effort = firefox_auto_script.set_estimated_effort
set_comment = firefox_auto_script.set_comment
set_effort = firefox_auto_script.set_effort
set_long_description = firefox_auto_script.set_long_description
set_short_description = firefox_auto_script.set_short_description

go_to_my_last_changed_tickets = firefox_auto_script.go_to_my_last_changed_tickets
go_to_notifications = firefox_auto_script.go_to_notifications

go_to_ms_home = firefox_auto_script.go_to_ms_home
go_to_pts_agile = firefox_auto_script.go_to_pts_agile
add_web_component = firefox_auto_script.add_web_component

scroll_down = firefox_auto_script.scroll_down
scroll_up = firefox_auto_script.scroll_up
close_ms_home_tab = firefox_auto_script.close_ms_home_tab
close_browser = firefox_auto_script.close_browser


session_feedback = ""

@app.route('/get_transcription', methods=['GET'])
def get_transc():
    transcription, _, _ = live.get_data()
    return transcription

@app.route('/get_prediction', methods=['GET'])
def get_pred():
    _, prediction, _ = live.get_data()
    return prediction

@app.route('/get_pipeline_feedback', methods=['GET'])
def get_pipeline_feedback():
    _, _, pipeline_feedback = live.get_data()
    return pipeline_feedback

@app.route('/get_feedback', methods=['GET'])
def get_pred_feedback():
    return firefox_auto_script.feedback

@app.route('/get_session_feedback', methods=['GET'])
def get_session_feedback():
    return session_feedback

@app.route('/run_script', methods=['GET'])
def run_script():
    try:
        session_feedback=""
        _, prediction = live.get_data()
        exec(prediction)
        return jsonify({'message': 'Script run successfully'})
    except:
        session_feedback = "Failed to run script"
        return  jsonify({'message': 'Failed to run script'})

@app.route('/record_with_time_out', methods=['POST'])
def record_transcribe_predict():
    try:
        session_feedback=""
        live.record_with_time_out()
        return jsonify({'message': 'Recorded successfully'})
    except:
        session_feedback = "Something went wrong!"

# ....
@app.route('/post_text_input', methods=['POST'] )
def get_form_input():
    text_input = request.form["textInput"]
    live.transcription = text_input

    return render_template('index.html')

@app.route('/only_pred', methods=['POST'])
def onlu_pred():
    live.only_pred()
    return jsonify({'message': 'Only pred successfully'})
# ....

@app.route('/connect_to_pts_via_firefox',  methods=['GET'])
def start_pts_with_selenium():
    try:
        session_feedback=""
        firefox_auto_script.driver= webdriver.Firefox()  
        firefox_auto_script.run_pts_with_selenium()
        firefox_auto_script.login(os.getenv("user_name"), os.getenv("password"))
        return jsonify({'status': 'Starting the PTS vocal commands session'})
    except:
        session_feedback = "Error while starting a Firefox vocal session!"

@app.route('/connect_to_pts_via_chrome',  methods=['GET'])
def start_pts_with_selenium_chrome():
    try:
        session_feedback=""
        firefox_auto_script.driver= webdriver.Chrome()  
        firefox_auto_script.run_pts_with_selenium()
        firefox_auto_script.login(os.getenv("user_name"), os.getenv("password"))
        return jsonify({'status': 'Starting the PTS vocal commands session'})
    except:
        session_feedback = "Error while starting a Chrome vocal session!"

@app.route('/change_language', methods=['POST'])
def change_language():
    lang = asr_model.get_language()
    if lang == 'En':
        asr_model.set_language('Tu')
    else:
        asr_model.set_language('En')

    lang= asr_model.get_language()

    return lang

if __name__ == "__main__":
    app.run(debug=True)


