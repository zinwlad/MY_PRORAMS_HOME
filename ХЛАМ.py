import json

def load_checklist():
    file_path = 'H:\\Python PROGRAMS\\untitled\\TestAssistant\\data\\web_data\\checklist.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        checklist = json.load(file)
    return checklist