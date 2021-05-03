import threading


class Messenger(threading.Thread):     # threading.Thread is a parent class and Messenger is inheriting from this class
    def run(self):          # run is a function specific to threads. whenever we create a thread we call this function
        for _ in range(10):   # it only loops 10 times and no variable is required
            # making two threads and giving them different names and printing their names
            print(threading.currentThread().getName())


# you can multiple objects from this class running at the same time
# concept of multithreading
x = Messenger(name="Send out message") # 1st thread and name gives name of thread
y = Messenger(name="Receive message")
x.start()           # this searches for run function in messenger and runs it
y.start()


