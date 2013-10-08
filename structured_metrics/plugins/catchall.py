from . import Plugin


class CatchallPlugin(Plugin):
    priority = -5
    """
    Turns metrics that aren't matched by any other plugin in something a bit more useful (than not having them at all)
    Another way to look at it is.. plugin:catchall is the list of targets you can better organize ;)
    Note that the assigned tags (i.e. source tags) are best guesses.  We can't know for sure!
    (this description goes for all catchall plugins)
    """

    targets = [
        {
            'match': '^(?P<n1>[^\.=]+)\.?(?P<n2>[^\.=]*)\.?(?P<n3>[^\.=]*)\.?(?P<n4>[^\.=]*)\.?(?P<n5>[^\.=]*)\.?(?P<n6>[^\.=]*)\.?(?P<n7>[^\.=]*)$',
            'target_type': 'unknown',
            'configure': [
                lambda self, target: self.add_tag(target, 'what', 'unknown'),
                lambda self, target: self.add_tag(target, 'source', 'unknown')
            ]
        },
    ]


# vim: ts=4 et sw=4:
