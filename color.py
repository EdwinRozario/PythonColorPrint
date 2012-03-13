class ColorPrint:

    def __init__(self, text):
        self.text = text
        self.color_codes = {
            'green' : '\033[1;32m%s\033[1;m',
            'blue' : '\033[1;34m%s\033[1;m',
            'gray' :'\033[1;30m%s\033[1;m',
            'red' : '\033[1;31m%s\033[1;m',
            'yellow' : '\033[1;33m%s\033[1;m',
            'magenta' : '\033[1;35m%s\033[1;m',
            'cyan' : '\033[1;36m%s\033[1;m',
            'white' : '\033[1;37m%s\033[1;m',
            'crimson' : '\033[1;38m%s\033[1;m',
            'RED' : '\033[1;41m%s\033[1;m',
            'GREEN' : '\033[1;42m%s\033[1;m',
            'BROWN' : '\033[1;43m%s\033[1;m',
            'BLUE' : '\033[1;44m%s\033[1;m',
            'MAGENTA' : '\033[1;45m%s\033[1;m',
            'CYAN' : '\033[1;46m%s\033[1;m',
            'GRAY' : '\033[1;47m%s\033[1;m',
            'CRIMSON' : '\033[1;48m%s\033[1;m'
            }

    def __getattr__(self, color):
        if (self.color_codes.has_key(color)):
            print self.color_codes[color] % self.text
        else:
            print self.text
