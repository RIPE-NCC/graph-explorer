from . import Plugin


class RipeDnsPlugin(Plugin):
    """Collect metrics for name servers.

    Works with diamond's bind collector
    """
    targets = [
        {
            'match': '^servers\.(?P<server>[^\.]+)\.bind\.view\.(?P<view>.+)\.(?P<category>[^\.]+)\.(?P<name>.*)$',
            'target_type': 'counter',
        },
        {
            'match': '^servers\.(?P<server>[^\.]+)\.bind\.(?P<category>[^\.]+)\.(?P<name>.*)$',
            'target_type': 'counter',
        },
    ]

    def sanitize(self, target):
        cat = target['tags']['category']
        
        if cat == 'sockstat':
            what = 'connections'
        elif cat == 'queries':
            what = 'queries'
        elif cat == 'nsstat':
            what = 'queries'
        elif cat == 'resstat':
            what = 'results'
        else:
            what = 'unknown'

        target['tags']['what'] = what

# vim: ts=4 et sw=4:
