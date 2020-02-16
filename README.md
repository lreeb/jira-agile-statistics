# jira-agile-statistics

This resulted out of a script to get some Sprint Statistics out of our Jira Board with Agile Plugin, 
using the Python Jira Rest Client (https://github.com/pycontribs/jira) and relying on custom JQL queries. 

Since Jira is abundantly customizable and used in very different ways it is not an out-of-the box project that will run for everyone. 
This is mainly provided as a starting point to customize and adapt to your own Jira configuration.

## Usage
* add Jira information in config.py
* define your sprints in sprint_data.json
* (possibly adjust queries in util/JiraQuery.py)
```bash
python run.py

```
## License
[MIT](https://choosealicense.com/licenses/mit/)
