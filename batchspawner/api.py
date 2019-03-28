import json
from tornado import web
from jupyterhub.apihandlers import  APIHandler, default_handlers

class BatchSpawnerAPIHandler(APIHandler):
    @web.authenticated
    def post(self):
        """POST set user spawner data"""
        token = self.get_auth_token()
        user = self.current_user
        data = self.get_json_body()
        spawner = user.spawner
        for x in user.spawners.values():
            if x.api_token == token:
                spawner = x
                break
        for key, value in data.items():
            if hasattr(spawner, key):
                setattr(spawner, key, value)
        self.finish(json.dumps({"message": "BatchSpawner data configured"}))
        self.set_status(201)

default_handlers.append((r"/api/batchspawner", BatchSpawnerAPIHandler))
