# -- General Packages --
import os
import datetime


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def str_to_datetime(time):
    """Convert a string to a datetime based on the format H:M"""
    return datetime.datetime.strptime(time, '%H:%M').time()


def read_interval_activation():
    """Read the last time interval in the txt file
       it keeps the two first values which are the start and the stop
       time in a string format"""
    # curr_path = os.path.dirname(__file__)
    curr_path = "/home/alex/Documents/improve_myself/internet_usage/"
    file_path = os.path.join(curr_path, "activation_time_list.txt")
    with open(file_path, 'r') as f:
        try:
            return f.readlines()[-1].split(',')[:2]
        except IndexError:
            raise ValueError("There is no data in the file")


def read_activation_time():
    """Extract the string value of the start and stop intervall"""
    interval = read_interval_activation()
    start = str_to_datetime(interval[0])
    stop = str_to_datetime(interval[1])
    return start, stop


def activate_or_deactivate_internet():
    """Activate the internet if the current time is inside the interval
       sent from the GUI is """
    current = datetime.datetime.now().time()
    # start = datetime.time(8, 34, 0)
    # stop = datetime.time(10, 40, 0)
    try:
        start, stop = read_activation_time()
        print(start, stop)

        # Block internet si on est dans la periode de travail
        if time_in_range(start, stop, current):
            print("activate internet")
            # Activation comes from the GUI
            os.system("rfkill unblock 1")
            # os.system("sudo ifconfig wlp3s0 up")
        else:   # TODO: Alexm: do a elif Internet is activated then kill it (so that you dont kill it everytime
            print("deactivate internet")
            os.system("rfkill block 1")
            # os.system("sudo ifconfig wlp3s0 down")
    except ValueError:
        print("there is not interval in the file")


if __name__ == '__main__':
    read_activation_time()
    activate_or_deactivate_internet()

