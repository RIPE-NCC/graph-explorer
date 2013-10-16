from . import Plugin


class RipeDnsPlugin(Plugin):
    """Collect metrics for name servers.

    Works with diamond's bind collector
    """
    targets = [
        {
            'match': '^servers\.(?P<server>[^\.]+)\.bind\.view\.(?P<view>.+)\.(?P<category>[^\.]+)\.(?P<what>.*)$',
            'target_type': 'counter',
        },
        {
            'match': '^servers\.(?P<server>[^\.]+)\.bind\.(?P<category>[^\.]+)\.(?P<what>.*)$',
            'target_type': 'counter',
        },
    ]

# vim: ts=4 et sw=4:
