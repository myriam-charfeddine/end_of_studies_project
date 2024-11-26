import json
import re
import torch
import google.generativeai as genai
from scripts import scripts

#"gemini-1.5-pro-latest"
class GeminiPromptEngineer:
    def __init__(self, model_name='gemini-pro' , torch_dtype=torch.float16, device=None): #gemini-1.5-flash
        try:
            self.api_key = ""   #Should have a token, the free use of Gemini LLM model is limited (1500 requests/day)
            genai.configure(api_key = self.api_key)
            self.model = genai.GenerativeModel(model_name)

        except Exception as e:
            print(f"Error configuring the Gemini API: {e}")


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
            
            response = self.model.generate_content(
               PROMPT,
               generation_config=genai.types.GenerationConfig(temperature=0))
            
            # print("Prediction: ", response.text)
            return response.text
        except Exception as e:
            # print(f"Error predicting script details: {e}")
            return {"method": None, "script": None}


