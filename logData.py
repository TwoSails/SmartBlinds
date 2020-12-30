"""
A program that records a log of data in order to assist debugging during an anomally and to help show recent moves
Able to help get the required number of steps for config.py
"""
import time
import json

count = 0


def shutdownLog(blindState):
    actualTime = time.asctime()
    state = blindState
    data = {}
    data["time"] = actualTime
    data["currentState"] = state

    file = open("home/pi/Documents/SmartBlinds/shutdown.json", "w")
    json.dump(data, file, indent=2)
    file.close()


def makeData(count, blindState, stepsCompleted, timeStart, timeEnd):
    count += 1
    actualTime = time.asctime()
    state = blindState
    steps = stepsCompleted
    timeTaken = timeEnd - timeStart
    data = {}
    data["time"] = actualTime
    data["currentState"] = state
    data["stepsCompleted"] = steps
    data["timeTaken"] = timeTaken
    data["count"] = count

    filename = "home/pi/Documents/SmartBlinds/logs/" + actualTime.replace(' ', '-') + ".json"

    file = open(filename, "w")
    json.dump(data, file, indent=2)
    file.close()


def loadLog():
    file = open("home/pi/Documents/SmartBlinds/shutdown.json", )
    data = json.load(file)
    file.close()
    currentState = data["currentState"]
    logs = open("home/pi/Documents/SmartBlinds/pastShutdownLog.json", 'a')
    json.dump(data, logs, indent=2)

    return currentState
