__author__ = 'pablo'
import re


class DownloadEngine:
    def __init__(self, url, plugin, reg_expr_pattern):
        if url is None or plugin is None or reg_expr_pattern is None:
            raise ValueError("Url, plugin and regular expression must be not None")

        self.url = url
        self.plugin = plugin
        self.reg_expr_pattern = reg_expr_pattern
        self.regular_expression_match = None
        self.name = None
        self.engine = None

    @property
    def is_valid(self):
        if self.regular_expression_match is None:
            regular_expression = re.compile(self.reg_expr_pattern)
            self.regular_expression_match = regular_expression.match(self.url)

        if self.regular_expression_match is not None and len(self.regular_expression_match.groups()) == 2:
            print(self.regular_expression_match)
            print(self.regular_expression_match.groups())
            print(self.regular_expression_match.group(2))
            return True
        else:
            return False

    def prepare_engine(self):
        if self.is_valid:
            self.name = self.regular_expression_match.group(2)
            self.engine = self.get_class(self.plugin)
            print("NAME->{} - ENGINE->{}".format(self.name, self.engine))
        else:
            raise RuntimeError('DownloadEngine is in an invalid state')

    def get_class(self, class_fullname):
        parts = class_fullname.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m

    def __str__(self):
        return "[Download Engine] - URL: {} - PLUGIN: {}".format(self.url, self.plugin)