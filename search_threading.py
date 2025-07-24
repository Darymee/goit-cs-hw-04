import threading
import time
from utils import search_keywords_in_files


def threaded_search(files, keywords, num_threads=4):
    print("\nTHREADING MODE STARTED...")
    start_time = time.time()
    result_dict = {word: [] for word in keywords}
    lock = threading.Lock()
    threads = []

    chunk_size = len(files) // num_threads + (len(files) % num_threads > 0)
    for i in range(num_threads):
        chunk = files[i * chunk_size : (i + 1) * chunk_size]
        thread = threading.Thread(
            target=search_keywords_in_files, args=(chunk, keywords, result_dict, lock)
        )
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()

    print(f"THREADING MODE COMPLETED in {time.time() - start_time:.2f} seconds")
    return result_dict
