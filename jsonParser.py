import json

def transform_text_to_json(file_path): 
    # loads json from a text file
    try:
        file = open(file_path,"r")
        for line in file:
            return line
    except:
        print("file doesn't exist")

def find_place_ids(json_list):

    ids = []
    names = []

    for dir in json_list["data"]:        
        id = dir["rootPlace"]["id"]
        name = dir["name"]

        ids.append(id)
        names.append(name)

    for i in range(len(ids)):
        try:
            print(str(ids[i]) + " " + str(names[i]))
        except:
            print("err")

    return ids

def write_text_in_json(file_path, data):
    # writes the data in a json file
    try:
        file = open(file_path, "w")
        file.write(data)
    except:
        print("file doesn't exist")

def write_array_in_file(file_path, data_list):
    try:
        file = open(file_path, "w")
        for dat in data_list:
            file.write(str(dat)+"\n")
    
    except:
        print("file doesn't exist")

def start():
    json_text = transform_text_to_json('json_test.txt')
    loaded_json = json.loads(json_text)

    indented_json_result = json.dumps(loaded_json, indent=4, sort_keys=True) # indents the json
    write_text_in_json("result.json",indented_json_result) # writes it in a file

    write_array_in_file("gamedat/placeids.txt",find_place_ids(loaded_json))

if __name__ == '__main__':
    start()