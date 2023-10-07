import time
import multiprocessing

def cpu_benchmark_test():
    start_time = time.time()
    
    # Get the number of available CPUs
    num_cpus = multiprocessing.cpu_count()
    
    # Create a list of CPU processes
    processes = []
    
    # Perform calculations in parallel with multiple processes
    for _ in range(num_cpus):
        process = multiprocessing.Process(target=perform_calculations)
        process.start()
        processes.append(process)
    
    # Wait for all processes to finish
    for process in processes:
        process.join()
    
    end_time = time.time()
    return end_time - start_time

def perform_calculations():
    # Perform a large number of calculations
    for _ in range(10**8):
        result = 2**2

benchmark_result = cpu_benchmark_test()
print(f"CPU Benchmark Test Result: {benchmark_result} seconds")
