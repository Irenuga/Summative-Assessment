from random import random, choice
from datetime import datetime

'''
This returns a random sensor reading
'''
def generate_sensor_reading():
    if random() < 0.01:
        return 'err'
    else:
        return random()
    

'''
This generates a random reading on the cluster
Sometimes, it returns an err
'''
def get_cluster_reading():
    readings = []

    for i in range(16):
        reading = []
        if not readings:
            reading = [generate_sensor_reading() for s in range(32)]
        else:
            if 'err' in readings[-1]:
                readings.append(['err']* 32)
                continue
            else:
                reading = [generate_sensor_reading() for j in range(32)]
        
        readings.append(reading)
    return readings

def create_error_log(dataset, timestamp):
    file = open('error.log', 'a+')
    for r in range(len(dataset)):
        if 'err' in dataset[r]:
            sensor_number = dataset[r].index('err')
            reading_number = r
            error_code = -999
            break
    file.write("%s, %s, %s, %s\n" % (
        timestamp, 
        error_code, 
        sensor_number, 
        reading_number
    ))

    file.close()


'''
This takes the reading from the readings from the sensor and writes it to file
'''
def read_sensor():
    file = open('dataset.csv', 'a+')
    timestamp = str(datetime.now())
    sensor_data = get_cluster_reading()
    file.write("%s|%s\n" % (timestamp, sensor_data))
    file.close()

    create_error_log(sensor_data, timestamp)

if __name__ == "__main__":
    read_sensor()