import os


def save_to_file(date_and_time, file_path, content):

    try:
        os.mkdir("data/output/" + date_and_time)
    except FileExistsError:
        pass

    with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
