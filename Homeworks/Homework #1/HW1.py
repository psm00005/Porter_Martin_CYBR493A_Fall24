## Porter Martin
## CYBR493A
## Fall24
## HW#1


print("Porter Martin, CYBR493A, Fall24, Homework #1")

import os
import time
from datetime import datetime

def method_name(parameter):
    result = parameter + 1
    return result

def ping_something(ip):
    ping_command = "ping " + ip
    ping_result = os.system(ping_command)
    return ping_result


def main():
    """
    Main function to prompt for an IP address and check if the host is responding.
    """
## List of IPS I found on a website for randomly selected IPS.
    ips = ["127.0.0.1", "8.8.8.8", "192.168.10.10", "1.1.1.1", "208.67.222.222", "4.2.2.2", "64.6.64.6", "69.162.81.155", "209.142.68.29", "206.71.50.230"]

## Using the code I currently had I asked ChatGPT this prompt for the "IF" statement "Can you code something that displays the total number of Ips that were reached successfully and the total number of Ips that were not pinged successfully, with this code:." The code referenced was just everything besides the "IF" statement.
    success_count = 0
    failure_count = 0

    for ip in ips:
        current_time = (datetime.now())
        result_from_method = ping_something(ip)
        ##print(result_from_method)
##Prints the number of times the ping failed or succeeded
        if result_from_method == 0:
            print(f"[{current_time}] Ping to {ip} Successful.")
            success_count += 1
        else:
            print(f"[{current_time}] Ping to {ip} Failed.")
            failure_count += 1
## Summarizes the total number of succesful and failed pings.
    print("\nSummary:")
    print(f"Total successful pings: {success_count}")
    print(f"Total failed pings: {failure_count}")

if __name__ == "__main__":
    main()

