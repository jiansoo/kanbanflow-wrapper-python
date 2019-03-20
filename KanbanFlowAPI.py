import requests
import json
import base64

class KanbanFlowWrapper:
    def __init__(self):
        self.url = 'https://kanbanflow.com/api/v1/'
        # Put your API Secret below, generated from the KanbanFlow website.
        self.api_secret = 'INSERT_API_SECRET_HERE'
        # Black magic to transmogrify API secret into base64 string, to be sent in the header of the request.
        self.headers = {'Authorization':'Basic '+ base64.b64encode(bytes('apiToken:'+self.api_secret, 'utf-8')).decode('UTF-8')}

    def _merge(self, dict1, dict2):
        # Merge function to allow header dictionaries to be merged. If there are any headers you would like to add,
        # you can just pass it as a param in sendRequest or sendPOST.
        merg = {**dict1, **dict2}
        return merg

    def sendPOST(self, destination, content, headers={}):
        # For POST requests.
        req = requests.post(self.url + destination, data=content, headers=self._merge(self.headers, headers))
        print(self.url + destination)
        return req

    def sendRequest(self, destination, headers={}):
        # For get requests.
        req = requests.get(self.url + destination, headers=self._merge(self.headers, headers))
        print(self.url + destination)
        return req

    def createTask(self, task, column, description=''):
        # Creates a task, given a description, columnId and name. 
        # Use getBoard() to get column info.
        content = {'name': task, 'columnId': column, 'description': description}
        req = self.sendPOST('tasks', content)
        return req

    def getBoard(self):
        # Gets board info in JSON format.
        req = self.sendRequest('board')
        return req

    def getTasks(self):
        # Gets JSON containing all tasks.
        req = self.sendRequest('tasks')
        return req
