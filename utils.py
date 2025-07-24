import os


def get_text_files(folder_path):
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder '{folder_path}' does not exist.")

    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.endswith(".txt") and os.path.isfile(os.path.join(folder_path, f))
    ]


def search_keywords_in_files(files, keywords, result_dict, lock=None):
    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                for word in keywords:
                    if word in content:
                        if lock:
                            with lock:
                                result_dict[word].append(file_path)
                        else:
                            result_dict[word].append(file_path)
        except Exception as e:
            print(f"Error - Failed to process file {file_path}: {e}")
