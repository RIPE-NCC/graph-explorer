from . import Plugin


class FilestatPlugin(Plugin):

    targets = [
        {
            'match': '^servers\.(?P<server>[^\.]+)\.files\.(?P<type>.*)$',
            'default_group_by': 'server',
            'target_type': 'gauge'
        },
    ]

# vim: ts=4 et sw=4:
