from filelock import FileLock
#install fileLock to run

with FileLock('/home/pi/Documents/test/sg0.jpg'):
    print("lock aquired")