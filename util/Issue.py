import dateutil.parser

class Issue:
    """ Wrapper class for jira issue that provides some additional methods """
    
    SECONDS_PER_HOUR = 3600.0
        
    def __init__(self, issue):
        self.issue = issue
        
    def get_storypoints(self):
        storypoints = self.issue.fields.customfield_10507
        if storypoints is not None:
            return storypoints
        else:
            return 0

    def get_hours(self):
        if self.issue.fields.timespent is not None:
            return self.issue.fields.timespent / self.SECONDS_PER_HOUR
        if self.issue.fields.timeestimate is not None:
            return self.issue.fields.timeestimate / self.SECONDS_PER_HOUR
        return 0
    
    def get_age(self):
        created = dateutil.parser.parse(self.issue.fields.created)
        resolved = dateutil.parser.parse(self.issue.fields.resolutiondate)
        return (resolved - created).days
    
    def is_bug(self):
        return self.issue.fields.issuetype.name == 'Bug'
    
    def is_interrupt(self):
        return self.issue.fields.issuetype.name == 'Interrupt'
    