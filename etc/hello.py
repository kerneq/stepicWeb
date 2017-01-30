import multiprocessing

bind = "0.0.0.0:8040"
workers = multiprocessing.cpu_count() * 2 + 1
