###### opening a file

# with open("notes.txt", "w") as file:
#     file.write("some list to do...")
#
# file = open("notes.txt", "w")
# try:
#     file.write("some todo...")
# finally:
#     file.close()

###### Creating a lock

# from threading import Lock
# lock = Lock()
#
# lock.acquire()
# #...
# lock.release()
#
# with lock:
#     #....

###### Implement content manager for classes

class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("exception has been handled")
        # print("exc:", exc_type, exc_val)
        print('exit')
        return True

with ManagedFile('notes.txt') as file:
    print("do some stuff...")
    file.write("some to dooo......")
    file.somemethod()
print('continuing')

