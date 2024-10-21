import threading
import time
import os

event = threading.Event()


def file_check(filename):
    while True:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    if "WOW" in line:
                        print(f"WOW found in {filename}!")
                        event.set()
                        return
            print(
                f'File {filename} find, but word "WOW" didn`t fine! Waiting 5 seconds'
            )
        else:
            print(f"{filename} not found. Waiting 5 seconds")
        time.sleep(5)


def file_remover(filename):
    print(f"Waiting for event to remove {filename}")
    event.wait()
    os.remove(filename)
    print(f"{filename} Deleted")


def main():
    file_name = "test_file.txt"
    finder_thread = threading.Thread(target=file_check, args=(file_name,))
    remover_thread = threading.Thread(target=file_remover, args=(file_name,))

    finder_thread.start()
    remover_thread.start()

    finder_thread.join()
    remover_thread.join()


if __name__ == "__main__":
    main()
