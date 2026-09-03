import time

def insertion_sort(dataInput):
    data = dataInput.copy()
    start = time.perf_counter()  
    for i in range(1, len(data)):
        current = data[i]
        j = i-1

        while j >= 0 and data[j] > current:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = current

    end = time.perf_counter()
    process_time = end - start
    return data, process_time


if __name__ == "__main__":
    import random
    sample_data = [random.randint(1, 10_000) for _ in range(1_000)]
    sorted_data, duration = insertion_sort(sample_data)
    print(f"Sorted {len(sorted_data)} items in {duration:.6f} seconds.")
