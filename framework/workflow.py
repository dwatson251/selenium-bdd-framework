import requests

from step_definitions.common.forms import fill_out_form
from framework.helper.LocalStorage import LocalStorage


class Workflow:

    def __init__(self, context, profile):
        # get the local storage
        storage = LocalStorage(context.navigator.browser)

        print(storage.get('authentication_token'))

        self.context = context
        self.profile = profile
        self.authentication_token = storage.get('authentication_token')['token']
        self.client_id = storage.get('authentication_token')['client_id']
        self.workflow_id = storage.get('authentication_token')['workflow_id']

        print(self.authentication_token)

        return

    def get_tasks(self):
        """Grabs a list of tasks from the API
        :return:
        """
        workflow_tasks_response = requests.get(
            self.context.api_url + '/clients/{client_id}/workflows/{workflow_id}/tasks/'
            .format(client_id=self.client_id, workflow_id=self.workflow_id))
        return workflow_tasks_response.json()

    def complete_task(self, task_name):
        """ Attempt to fill in a task, given a name matching the form on the profile json file
        :param task_name:
        :return:
        """
        fill_out_form(self.context, task_name, self.profile)
        return

    def complete_my_details(self):
        """Custom method to handle a task in case special actions are needed
        """
        return

    def complete(self):
        for task in self.get_tasks():
            task_name = task['workflow_task']['task_name']
            self.complete_task(task_name)

        return
