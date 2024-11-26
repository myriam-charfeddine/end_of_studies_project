from typing import Dict, TypedDict

# ..............Graph State...................
class State(TypedDict):
    to_pts: bool
    transcription: str
    predicted_script: str