from ninfo import PluginBase
from ninfo import util
import ieeemac

class jira_plug(PluginBase):
    """Search Jira for issues"""
    name          = 'jira'
    title         = 'Jira'
    description   = 'Jira'
    cache_timeout = 60*60
    types         = ['ip','ip6', 'hostname', 'mac']
    remote       = False

    def setup(self):
        from jira.client import JIRA
        server = self.plugin_config["server"]
        user   = self.plugin_config["user"]
        pw     = self.plugin_config["password"]
        proj   = self.plugin_config["project"]

        self.field_ip   = self.plugin_config.get("field_ip", "IP")
        self.field_mac  = self.plugin_config.get("field_mac", "MAC")
        self.field_hn   = self.plugin_config.get("field_hostname", "FQDN")

        self.jira = JIRA(options={'server': server}, basic_auth=(user, pw))
        self.project = proj

    def get_info(self, arg):
        if util.get_type(arg) == "mac":
            field = self.field_mac
            #work around jira being dumb:
            #Unable to parse the text '00:11:22:33:44:55' for field 'MAC Address'.
            arg = ieeemac.Mac(arg).to_unix.replace(":", " ")
        elif util.get_type(arg) == 'hostname':
            field = self.field_hn
        else:
            field = self.field_ip

        q = 'project="%s" AND "%s" ~ "%s"' % (self.project, field, arg)
        issues = self.jira.search_issues(q)

        issue_dicts = [issue.raw for issue in issues]
        return {"issues": issue_dicts}

plugin_class = jira_plug
