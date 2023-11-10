import redis
import os


def Redis():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.flushall()
    r.flushdb()

    # open colors.csv
    with open(os.path.join(os.path.dirname(__file__), 'colors.csv')) as c:
        for line in c:
            # split line into list
            line = line.split(',')
            # add color to redis
            r.set(line[0], line[1].strip())


if__name__ == '__main__':
    Redis()
