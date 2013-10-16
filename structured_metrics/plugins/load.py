from . import Plugin


class LoadPlugin(Plugin):
    targets = [
        {
            'match': '^servers\.(?P<server>[^\.]+)\.loadavg\.(?P<wt>.*)$',
            'target_type': 'gauge'
        }
    ]

    def sanitize(self, target):
        if target['tags']['wt'] in ('01','05','15','load'):
            target['tags']['what'] = 'load'
            target['tags']['type'] = target['tags']['wt']
        if target['tags']['wt'] in ('processes_running', 'processes_total'):  # this should be ev. else
            (target['tags']['what'], target['tags']['type']) = target['tags']['wt'].split('_')
        del target['tags']['wt']
# vim: ts=4 et sw=4:
