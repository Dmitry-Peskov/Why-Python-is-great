import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"С момента запуска таймера прошло {elapsed_time} секунд")
        del self


if __name__ == "__main__":

    with Timer():
        # здесь мы получили экземпляр класса Timer
        time.sleep(3)
    # здесь работа с таймером была завершена

    with Timer():
        # здесь мы получили новый экземпляр класса Timer
        time.sleep(1)
    # здесь работа с таймером была завершена
