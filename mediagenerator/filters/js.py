from mediagenerator.generators.bundles.base import Filter


class AddSemicolonFilter(Filter):
    def __init__(self, **kwargs):
        super(AddSemicolonFilter, self).__init__(**kwargs)
        assert self.filetype == 'js', (
            'AddSemicolonFilter only handles JavaScript files. '
            'The parent filter expects "%s".' % self.filetype)

    def get_output(self, variation):
        for input in self.get_input(variation):
            yield u'{0};'.format(input)
