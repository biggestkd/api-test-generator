import os


def save_to_file(datetime, file_path, content):

    try:
        os.mkdir("data/output/" + datetime)
    except FileExistsError:
        pass

    with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
