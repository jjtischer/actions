import json

class ActionObj:
    def __init__(self, action, time):
        self.action = action
        self.time = []
        self.time.append(time)
        self.avg = time

    def addTime(self, time):
        self.time.append(time)
        self.avg = int(sum(self.time)/len(self.time))
        return self.avg

class ActionsLib:
    def __init__(self):
        pass

    list = []

    def findActionIndex(self, name):
        for i, a in enumerate(self.list, start=0):
            if name == a.action:
                return i
        return -1

    def parseJson(self, action_json):
        try:
            parseAction = json.loads(action_json)
        except json.decoder.JSONDecodeError:
            raise Exception('Error: addAction: invalid json object')

        if 'action' not in parseAction.keys():
            raise Exception('Error: invalid json action missing')
        if 'time' not in parseAction.keys():
            raise Exception('Error: invalid json time missing')
        return parseAction

    def addAction(self, action_json):
        action = self.parseJson(action_json)
        name = action['action']
        value = action['time']

        index = self.findActionIndex(name)
        if index < 0:
            self.list.append(ActionObj(name, value))
        else:
            self.list[index].addTime(value)
        return self.list

    def getStats(self):
        #translating the object to ensure expected output
        action_list = []
        for obj in self.list:
            action_item = {"action": "", "avg": ""}
            action_item['action'] = obj.action
            action_item['avg'] = obj.avg
            action_list.append(action_item)
        return action_list