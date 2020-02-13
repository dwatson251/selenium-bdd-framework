import json


class Routes:

    def __init__(self, context, routes_file_path):
        """
        Obtains a route from a specified route source

        :param context:
        :param routes_file_path:
        """
        self.context = context

        with open(routes_file_path, 'r') as f:
            self.profile = json.load(f)

    def get_route(self, name):
        """
        Creates a fully usable URL from the route using the base URL in the config and a defined route

        :param name:
        :return:
        """

        route = self.context.base_url + '/' + self.profile[name]
        return route
