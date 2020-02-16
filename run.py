# -*- coding: UTF-8 -*-
from jira import JIRA
import json
import matplotlib.pyplot as plt

from config import *
from util.Issue import Issue
from util.JiraQuery import JiraQuery
from util.Sprint import Sprint


jiraQuery = JiraQuery(jira_options, jira_user, jira_pwd, project)

def create_sprint(s):
    return Sprint(s["name"], s["start"], s["end"], jiraQuery)

def load_sprints():
    with open('sprint_data.json', 'r') as f:
        sprint_data = json.load(f)
    return list(map(create_sprint, sprint_data))

def create_plot():
    fig, axs = plt.subplots(3, 2)
    fig.tight_layout(pad=1.8)
    fig.set_figwidth(9)
    fig.set_figheight(9)

    axs[0, 0].set_title('Sprint velocity')
    axs[0, 0].plot(range(len(sprints)), list(map(lambda s: s.get_finished_velocity(), sprints)), 'go-')
    axs[0, 0].set_xticks(range(len(sprints)))
    axs[0, 0].set_xticklabels(list(map(lambda s: s.sprint_name, sprints)), rotation=30)
    axs[0, 0].set_ylabel('Storypoints')

    axs[0, 1].set_title('Bug velocity')
    axs[0, 1].plot(range(len(sprints)), list(map(lambda s: s.get_bug_velocity(), sprints)), 'bo-')
    axs[0, 1].set_xticks(range(len(sprints)))
    axs[0, 1].set_xticklabels(list(map(lambda s: s.sprint_name, sprints)), rotation=30)
    axs[0, 1].set_ylabel('Storypoints')

    axs[1, 0].set_title('Sprint target deviation')
    axs[1, 0].bar(range(len(sprints)), \
              list(map(lambda s: s.get_finished_minus_planned(), sprints)), \
              align='center', \
              alpha=0.5, \
              color=list(map(lambda s: 'g' if s.get_finished_minus_planned() >= 0 else 'r', sprints)))
    axs[1, 0].set_xticks(range(len(sprints)))
    axs[1, 0].set_xticklabels(list(map(lambda s: s.sprint_name, sprints)), rotation=30)
    axs[1, 0].set_ylabel('Storypoints')

    axs[1, 1].set_title('Bugs opened')
    axs[1, 1].bar(range(len(sprints)), list(map(lambda s: s.get_bugs_opened(), sprints)), align='center', alpha=0.5, color='r')
    axs[1, 1].set_xticks(range(len(sprints)))
    axs[1, 1].set_xticklabels(list(map(lambda s: s.sprint_name, sprints)), rotation=30)
    axs[1, 1].set_ylabel('# Bugs')

    axs[2, 0].set_title('Average issue size')
    axs[2, 0].bar(range(len(sprints)), list(map(lambda s: s.get_average_storysize(), sprints)), align='center', alpha=0.5)
    axs[2, 0].set_xticks(range(len(sprints)))
    axs[2, 0].set_xticklabels(list(map(lambda s: s.sprint_name, sprints)), rotation=30)
    axs[2, 0].set_ylabel('Storypoints')
    
    axs[2, 1].set_title('Average issue age')
    axs[2, 1].bar(range(len(sprints)), list(map(lambda s: s.get_average_age(), sprints)), align='center', alpha=0.5)
    axs[2, 1].set_xticks(range(len(sprints)))
    axs[2, 1].set_xticklabels(list(map(lambda s: s.sprint_name, sprints)), rotation=30)
    axs[2, 1].set_ylabel('Days')

    plt.show()

if __name__ == "__main__":
    sprints = load_sprints()
    create_plot()

