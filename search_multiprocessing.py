import multiprocessing
import time
from multiprocessing import Manager
from utils import search_keywords_in_files


def multiprocessing_search(files, keywords, num_processes=4):
    print("\nMULTIPROCESSING MODE STARTED...")
    start_time = time.time()
    manager = Manager()
    result_dict = manager.dict({word: manager.list() for word in keywords})
    processes = []

    chunk_size = len(files) // num_processes + (len(files) % num_processes > 0)
    for i in range(num_processes):
        chunk = files[i * chunk_size : (i + 1) * chunk_size]
        p = multiprocessing.Process(
            target=search_keywords_in_files, args=(chunk, keywords, result_dict)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    final_result = {word: list(result_dict[word]) for word in keywords}
    print(f"MULTIPROCESSING MODE COMPLETED in {time.time() - start_time:.2f} seconds")
    return final_result
