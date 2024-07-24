def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except IOError:
        return None

def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return True
    except IOError:
        return False

filter_file = "filter.txt"
filter_content = read_file(filter_file)
if filter_content:
    words_to_remove = [word.strip().lower() for word in filter_content.split(',')]
else:
    print("Failed to read filter file.")
    exit()

dictionary_file = "en_US.dic"
content = read_file(dictionary_file)
if content:
    lines = [line for line in content.split('\n') if not any(word.lower() in line.lower() for word in words_to_remove)]
    updated_content = '\n'.join(lines)
    if write_file(dictionary_file, updated_content):
        print("Deleted all the bad words!")
    else:
        print("Failed to remove words. omfg must be a permissions issue....")
else:
    print("Failed to read dictionary file.")

