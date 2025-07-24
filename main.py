from utils import get_text_files
from search_threading import threaded_search
from search_multiprocessing import multiprocessing_search


def print_results(title, results):
    print(f"\nRESULTS - {title}")
    for word, files in results.items():
        print(f"{word}: {files}")


def main():
    folder = "text_files"
    keywords = ["Google", "keywords", "test", "5", "undefined"]

    try:
        files = get_text_files(folder)
    except FileNotFoundError as e:
        print(e)
        return

    if not files:
        print("No .txt files found.")
        return

    result_threads = threaded_search(files, keywords)
    print_results("THREADING", result_threads)

    result_processes = multiprocessing_search(files, keywords)
    print_results("MULTIPROCESSING", result_processes)


if __name__ == "__main__":
    main()
