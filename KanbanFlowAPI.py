import requests
import json
import base64

class KanbanFlowWrapper:
    def __init__(self):
        self.url = 'https://kanbanflow.com/api/v1/'
        self.api_secret = 'INSERT_API_SECRET_HERE'
        self.headers = {'Authorization':'Basic '+ base64.b64encode(bytes('apiToken:'+self.api_secret, 'utf-8')).decode('UTF-8')}

    def merge(self, dict1, dict2):
        merg = {**dict1, **dict2}
        return merg

    def sendPOST(self, destination, content, headers={}):
        req = requests.post(self.url + destination, data=content, headers=self.merge(self.headers, headers))
        print(self.url + destination)
        return req

    def sendRequest(self, destination, headers={}):
        req = requests.get(self.url + destination, headers=self.merge(self.headers, headers))
        print(self.url + destination)
        return req

    def createToDoTask(self, task, column, description=''):
        content = {'name': task, 'columnId': column, 'description': description}
        req = self.sendPOST('tasks', content)
        return req

    def getBoard(self):
        req = self.sendRequest('board')
        return req

    def getTasks(self):
        req = self.sendRequest('tasks')
        return req
