import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"С момента запуска таймера прошло {elapsed_time} секунд")


if __name__ == "__main__":
    with Timer() as timer:
        time.sleep(3)

    with Timer() as timer2:
        time.sleep(1)
