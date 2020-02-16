from jira import JIRA
from util.Issue import Issue

class JiraQuery:
    """Util class for performing JQL queries"""
    
    MAX_RESULTS = 1000000
    
    def __init__(self, jira_options, jira_user, jira_pwd, project):
        self.jira=JIRA(options=jira_options,basic_auth=(jira_user,jira_pwd))
        self.project = project

    def planned_issues(self, sprint):
        print('Request to Jira Server: Planned Issues for sprint ' + sprint)
        issues = self.jira.search_issues(
            'project=\'' + self.project + '\' AND sprint = \'' + sprint + '\' ' + \
            'AND (type = Story OR type = Bug) ' + \
            'AND issueFunction not in addedAfterSprintStart(\'' + self.project + '\', \'' + sprint + '\')', \
            maxResults = self.MAX_RESULTS)
        return list(map(Issue, issues))
    
    def finished_issues(self, sprint):
        print('Request to Jira Server: Finished Issues for sprint ' + sprint)
        issues = self.jira.search_issues(
            'project=\'' + self.project + '\' AND sprint = \'' + sprint + '\' ' + \
            'AND ( type = Story or type = Bug or type = Interrupt) ' + \
            'AND status = Closed ' + \
            'AND issueFunction in completeInSprint(\'' + self.project + '\', \'' + sprint + '\')', \
            maxResults = self.MAX_RESULTS)
        
        return list(map(Issue, issues))

    def bugs_opened(self, sprint, sprint_start_date, sprint_end_date):
        print('Request to Jira Server: Bugs opened in sprint ' + sprint)
        issues = self.jira.search_issues(
            'project = \'' + self.project + '\' ' + \
            'AND type = Bug ' + \
            'AND created >= \'' + sprint_start_date + '\' ' + \
            'AND created <= \'' + sprint_end_date + '\' ',
            maxResults = self.MAX_RESULTS)
        return list(map(Issue, issues))

