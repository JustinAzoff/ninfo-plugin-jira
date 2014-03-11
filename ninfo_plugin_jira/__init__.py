from ninfo import PluginBase

class jira_plug(PluginBase):
    """Search Jira for issues"""
    name          = 'jira'
    title         = 'Jira'
    description   = 'Jira'
    cache_timeout = 60*60
    types         = ['ip','ip6','cidr', 'cidr6', 'hostname','username','hash']
    #local        = False
    #remove       = False

    def setup(self):
        pass

    def get_info(self, arg):
        return {}

plugin_class = jira_plug
