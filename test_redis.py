### To implement various use-cases of Redis and it's utilities

import redis
import logging


class Redis:

    def __init__(self):
        self.port = 6379
        self.host = 'localhost'

    def connect_to_redis(self):
        try:
            redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
            print("*** Successfully established connection with redis *** \n")
            return redis_client
        except Exception as ex:
            print(f"*** Unable to establish connection with redis: {ex} ***")

    def add_elements(self, lst, lst_elements=[]):
        try:
            redis_client = self.connect_to_redis()
            for ele in lst_elements:
                redis_client.rpush(lst, ele)
                print(f"*** Successfully add a new element to redis: {ele} *** \n")
        except Exception as ex:
            print(f"*** Unable to add new element to redis: {ex} *** \n")

    def get_stored_elements(self, lst_name):
        try:
            redis_client = self.connect_to_redis()
            stored_elements = redis_client.lrange(lst_name, 0, -1)
            print(f"*** Successfully fetched the stored elements in redis *** \n")
            return stored_elements
        except Exception as ex:
            print(f"*** Unable to fetch the elements stored in redis: {ex} *** \n")
    
    def delete_last_n_elements(self, lst, n):
        try:
            redis_client = self.connect_to_redis()
            redis_client.ltrim(lst, -n, -1)
            print(f"*** Successfully deleted the last {n} elements *** \n")
        except Exception as ex:
            print(f"*** Unable to delete the lst n elements stored in redis: {ex} *** \n")


if __name__ == '__main__':

    rds = Redis()
    lst = "lst"
    element_to_be_added = [1, 2, 3, 4, 5]

    rds.connect_to_redis()

    ### Leaving this function call (add_elements) commented, since every time the script is invoked, 
    ### the same elements are stored again in redis
    rds.add_elements(lst, element_to_be_added)

    stored_elements_before_deletion = rds.get_stored_elements(lst)
    print(f"*** Elements stored in redis before deletion: {stored_elements_before_deletion} ***\n")

    rds.delete_last_n_elements(lst, 5)

    stored_elements_after_deletion = rds.get_stored_elements(lst)
    print(f"*** Elements stored in redis after deletion: {stored_elements_after_deletion} ***")
