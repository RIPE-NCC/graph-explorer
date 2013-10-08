from . import Plugin


class RipeLogstashPlugin(Plugin):
    """
    """
    targets = [
        {
            'match': '^logs\.(?P<server>[^\.]+)\.(?P<cat>[^\.]+\.[^\.]+)\.(?P<what>.*)',
            'target_type': 'unknown',
            'configure': [
                lambda self, target: self.add_tag(target, 'source', 'logstash')
            ]
        },
    ]

    def sanitize(self, target):
        what = target['tags']['what']

        if what.endswith('_avg_time'):
            target['tags']['type'] = 'guage'
        elif what.endswith('_num_ops'):
            target['tags']['type'] = 'count'

# vim: ts=4 et sw=4:
