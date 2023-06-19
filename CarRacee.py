import threading 
import time
import sys

class Car:
    def __init__(self):
        self.place = 0    

class Race:
    def __init__(self):
        self.i = 0
        self.next_num = 0
        self.lock = threading.Lock()
        self.counters = [0] * 20
        self.places = [0] * 20
        # next_sum - amount of all laps done   

# A method that displays the number of laps for the car
    def print_laps(self, car_num):
        while self.counters[car_num-1] != 51:
            with self.lock:
                self.next_num += 1
                time.sleep(0.001)
                if(self.counters[car_num-1] == 50):
                    self.places[self.i] = car_num
                    self.i += 1

                self.counters[car_num-1] += 1
                print(f"Car {car_num}: {self.counters[car_num-1]}")

# A method that displays race results
    def print_counters(self):
        sorted_counters = sorted(enumerate(self.counters), key=lambda x: x[1], reverse=True)
        print("Race result:")
        for i, (car_index, counter) in enumerate(sorted_counters):
            position = i + 1
            car_num = car_index + 1
            print(f"{position}. Car {car_num}: {counter} laps")

    def print_places(self):
        print("Places: ")
        for i in range(20):
            print(f"Place {i+1}, car number: {self.places[i]}")

# Create an instance of the Race class
race = Race()

# Create an empty list of threads
threads = []

# Loop 20 times to create 20 threads
for i in range(20):
    thread = threading.Thread(target=race.print_laps, args=(i+1,))
    # Add the newly created thread to the list of threads
    threads.append(thread)
    # Start the thread
    thread.start()

# Loop through the list of threads and call the join() method 
# on each thread to wait for them to finish
for thread in threads:
    thread.join

#Display race results
time.sleep(5)

score = threading.active_count()
print(score)


print("\n")
race.print_counters()

print(race.next_num)

race.print_places()