
def average(list_of_ints):
    return sum(list_of_ints)/len(list_of_ints)


def sum_storypoints(issues):
    return sum(map(lambda x: x.get_storypoints(), issues))

class Sprint:
    
    def __init__(self, name, start_date, end_date, jiraQuery):
        self.sprint_name = name
        self.start_date = start_date
        self.end_date = end_date
        self.jiraQuery = jiraQuery

    def get_planned_velocity(self):
        return sum_storypoints(self._get_planned_issues())

    def get_finished_velocity(self):
        return sum_storypoints(self._get_finished_issues_with_storypoints())
    
    def get_finished_minus_planned(self):
        return self.get_finished_velocity() - self.get_planned_velocity()
    
    def get_average_storysize(self):
        storypoints = list(map(lambda x: x.get_storypoints(), self._get_finished_issues_with_storypoints()))
        return average(list(filter(lambda x: x > 0, storypoints)))
    
    def get_average_age(self):
        return average(list(map(lambda x: x.get_age(), self._get_finished_issues_with_storypoints())))

    def get_interrupt_hours(self):
        interrupts = filter(lambda x: x.is_interrupt(), self._get_finished_issues())
        return sum(map(lambda x: x.get_hours(), interrupts))
    
    def get_bug_velocity(self):
        return sum_storypoints(self._get_finished_bugs())

    def get_bugs_opened(self):
        if self._get_bugs_opened_in_sprint() is None:
            return 0
        return len(self._get_bugs_opened_in_sprint())
    
    def _get_finished_issues_with_storypoints(self):
        return list(filter(lambda x: not x.is_interrupt(), self._get_finished_issues()))
    
    def _get_finished_bugs(self):
        return list(filter(lambda x: x.is_bug(), self._get_finished_issues()))
    
    
    ''' queries are slow, the following methods save the results for re-use '''
    
    def _get_planned_issues(self):
        if not hasattr(self, 'planned_issues'):
            self.planned_issues = self.jiraQuery.planned_issues(self.sprint_name)
        return self.planned_issues
    
    def _get_finished_issues(self):
        if not hasattr(self, 'finished_issues'):
            self.finished_issues = self.jiraQuery.finished_issues(self.sprint_name)
        return self.finished_issues
    
    def _get_bugs_opened_in_sprint(self):
        if not hasattr(self, 'bugs_opened'):
            self.bugs_opened = self.jiraQuery.bugs_opened(self.sprint_name, self.start_date, self.end_date)
        return self.bugs_opened

        