import json

def transform_text_to_json(file_path): 
    # loads json from a text file
    try:
        file = open(file_path,"r")
        for line in file:
            return line
    except:
        print("file doesn't exist")

def write_text_in_json(file_path, data):
    # writes the data in a json file
    try:
        file = open(file_path, "w")
        file.write(data)
    except:
        print("file doesn't exist")

def start():
    json_text = transform_text_to_json('json_test.txt')
    loaded_json = json.loads(json_text)

    indented_json_result = json.dumps(loaded_json, indent=4, sort_keys=True) # indents the json
    write_text_in_json("result.json",indented_json_result) # writes it in a file

if __name__ == '__main__':
    start()