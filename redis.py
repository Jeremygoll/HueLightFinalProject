import csv
import redis

redis.client.StrictRedis(host='localhost', port=6379, db=0)

file_path = 'colors.csv'


def add_data_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            key = row['key']
            value = row['value']
            redis.set(key, value)

            if 'list_value' in row:
                list_key = key
                list_values = row['list_value'].split(',')
                # Push values to a list
                redis.rpush(list_key, *list_values)


if __name__ == "__main__":
    csv_file_path = 'colors.csv'
    add_data_from_csv(csv_file_path)
    print('Data added successfully')
    redis.close()
