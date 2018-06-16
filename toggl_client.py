import requests
import base64
import datetime

class TogglClient:

    def __init__(self, api_token):
        self.api_token = api_token
        self.params = {}
        self.__set_initial_params()

    def request(self, url, params = {}):
        """Request basics."""
        r = requests.Session()

        auth_header = self.api_token + ":" + "api_token"
        auth_header = "Basic {}".format(base64.b64encode(bytes(auth_header, "utf-8")).decode("ascii"))
        headers = {
            "Authorization": auth_header,
            "Content-Type": "application/json",
            "Accept": "*/*",
            "User-Agent": "togglore",
        }

        response = requests.get(url,headers=headers,params=params).json()

        return response

    def __set_initial_params(self):
        """Set mandaroty params"""
        response  = self.request('https://www.toggl.com/api/v8/me')
        workspace = self.__set_workspace(response)
        self.params = {'user_agent':response['data']['email'],'workspace_id':workspace}
    
    def __set_workspace(self, response):
        """Set active workspace"""
        workspace_ids_names = [{'name':item['name'],'id':item['id']} for item in response['data']['workspaces'] if item['admin']==True]
        
        if(len(workspace_ids_names) < 1):
            raise ValueError("You need one workspace at least")
        
        #TODO: Select only first workspace
        return workspace_ids_names[0]['id']

    def get_summary_results(self, start_date = '', until_date = ''):
        """Get summary results and calculate if inputs are showing"""
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        if not start_date:
            start_date = yesterday.strftime("%Y-%m-%d")
        if not until_date:
            until_date = yesterday.strftime("%Y-%m-%d")
        
        self.params['since']=start_date
        self.params['until']=until_date

        response = self.request('https://toggl.com/reports/api/v2/summary', self.params)

        if len(response['data']) > 0:
            return True
        else:
            return False

    
