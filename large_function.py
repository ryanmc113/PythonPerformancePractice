import time


@profile
def heavy_work():
    print("Do something")
    print("Do something")
    print("Do something")

    for _ in range(100_000_000):
        pass


start_time = time.time()
heavy_work()
end_time = time.time()
print(f"Duration: {end_time - start_time}")
