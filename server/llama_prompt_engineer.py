import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import json
import ollama 
from scripts import scripts

class LLaMAPromptEngineer:
    def __init__(self, model_name='llama3:instruct', torch_dtype=torch.float16, device=None):
        # try:
            # self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        #     self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch_dtype)
            self.device = device if device else torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            self.model_name = model_name
        #     self.model.to(self.device)
        #     print("LLaMA model loaded successfully.")
        # except Exception as e:
        #     print(f"Error loading LLaMA model: {e}")

    def extract_json_objects_from_string(self, input_str):
        stack = []
        json_str = ""
        inside_json = False
        json_objects = []
        
        for char in input_str:
            if char == '{':
                if not inside_json:
                    inside_json = True
                stack.append(char)
                json_str += char
            elif char == '}':
                if inside_json:
                    stack.pop()
                    json_str += char
                    if not stack:
                        inside_json = False
                        
                        try:
                            json_data = json.loads(json_str)
                            json_objects.append(json_data)
                            json_str = ""
                        except json.JSONDecodeError as e:
                            raise ValueError(f"Error decoding JSON: {e}")
            elif inside_json:
                json_str += char

        if not json_objects:
            raise ValueError("No JSON content found in the input string.")

        return json_objects
    
    def predict_endpoint_details(self, scripts_list, user_input):
        try:
            PROMPT = f""" 
                        Based on the provided scripts_list and user_input you should:

                        -Predict the right script
                        -Replace the params with the right values based on the user_input
                        -If a param is not specified, just ignore it
                        -The "nmber", "effort" and "estimated_effort" params are always numbers
                        -Always convert string numbers to integers. Example seven => 7, two => 2, fourteen => 14
                        -Output the function_name value and pass between the () each param name followed by = then the VALUE between "" of the param
                        -Think carefully and If you don't know the answer return None
                        -Don't invent new scripts, always refer to the provided list of scripts
                        -Don't invent new params to a script, always refer to the script existing params
                        -The returned result for each function should be the function_name value with the right params names and values between ()
                        
                        Output ONLY function_name, without any extra word or additional formatting or explanations.

                        scripts_list : {scripts_list}
                        user_input : {user_input}
            """
            response = ollama.chat(
                            model=self.model_name,
                            messages=[{'role': 'user', 'content': PROMPT}],
                            stream=False,
                            format='json'
                        )['message']['content']
            # json_response = self.extract_json_objects_from_string(response)
            # return json_response
            return response
        
        except Exception as e:
            print(f"Error predicting endpoint details: {e}")
            return {"endpoint_url": None, "method": None, "body_request": None}
