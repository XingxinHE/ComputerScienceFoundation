"""The buffer module assists in iterating through lines and tokens."""

import math
import sys

# BEGIN SOLUTION NO PROMPT
if sys.version_info[0] < 3:  # Python 2 compatibility
    def input(prompt):
        sys.stderr.write(prompt)
        sys.stderr.flush()
        line = sys.stdin.readline()
        if not line: raise EOFError()
        return line.rstrip('\r\n')
# END SOLUTION


class EOL_TOKEN:
    """
    A token that represents the end of a line in the Buffer's input source.
    """

    def __repr__(self):
        return "This is a token representing the end of a line."


# The following line of code makes a single instance of the class EOL_TOKEN.
# This single instance is what you will be referencing as EOL_TOKEN in Buffer.
EOL_TOKEN = EOL_TOKEN()


class Buffer:
    """A Buffer provides a way of accessing a sequence of tokens across lines.

    Its constructor takes an iterator, called "the source", that returns the
    next line of tokens as a list each time it is queried, or None to indicate
    the end of data.

    The Buffer in effect concatenates the sequences returned from its source
    and then supplies the items from them one at a time through its pop_first()
    method, calling the source for more sequences of items only when needed.

    In addition, Buffer provides a current instance attribute to look at the
    next item to be supplied, without sequencing past it.

    >>> buf = Buffer(iter([['(', '+'], [15], [], [12, ')']]))
    >>> buf.end_of_line()   # False since we have not reached the end of a line
    False
    >>> buf.current
    '('
    >>> buf.pop_first()
    '('
    >>> buf.current
    '+'
    >>> buf.pop_first()
    '+'
    >>> buf.end_of_line()   # We have reached the end of a line
    True
    >>> buf.current
    This is a token representing the end of a line.
    >>> buf.pop_first()
    This is a token representing the end of a line.
    >>> buf.current # Move onto the next line
    15
    >>> buf.pop_first()
    15
    >>> buf.current
    This is a token representing the end of a line.
    >>> buf.pop_first()
    This is a token representing the end of a line.
    >>> buf.current # This should be EOL_TOKEN, since this line is empty
    This is a token representing the end of a line.
    >>> buf.end_of_line()
    True
    >>> buf.pop_first()
    This is a token representing the end of a line.
    >>> buf.current
    12
    >>> buf.pop_first()
    12
    >>> buf.current
    ')'
    >>> buf.pop_first()
    ')'
    >>> buf.current
    This is a token representing the end of a line.
    >>> buf.pop_first()
    This is a token representing the end of a line.
    >>> buf.current         # returns None
    >>> buf.pop_first()     # returns None
    """

    def __init__(self, source):
        """
        Initialize a Buffer instance based on the given source.
        """
        # BEGIN SOLUTION NO PROMPT
        # To staff: the below code is for the read-eval-print loop
        # in the Scheme project, NOT needed for the lab.
        self.lines = []
        self.current_line = []
        # END SOLUTION

        # BEGIN SOLUTION
        self.token_gen = self.create_generator(source)
        self.current = next(self.token_gen, None)
        # END SOLUTION

    def create_generator(self, source):
        """
        Yield tokens from the source. At the end of every line of source input,
        yield EOL_TOKEN.
        """
        # BEGIN SOLUTION
        for line in source:
            for elem in line:
                yield elem
            yield EOL_TOKEN
        # END SOLUTION

    def pop_first(self):
        """
        Return the current token from self, and update the current token to
        be the next token. If there are no more tokens in the source, update
        the current token to be None.
        """
        # BEGIN SOLUTION
        current = self.current
        # END SOLUTION

        # BEGIN SOLUTION NO PROMPT
        # To staff: the below code is for the read-eval-print loop
        # in the Scheme project, NOT needed for the lab.
        if current is EOL_TOKEN:
            self.lines.append(self.current_line)
            self.current_line = []
        else:
            self.current_line.append(current)
        # END SOLUTION

        # BEGIN SOLUTION NO PROMPT
        self.current = next(self.token_gen, None)
        return current
        # END SOLUTION

    def end_of_line(self):
        return self.current is EOL_TOKEN

    def has_more(self):
        return self.current is not None

    # BEGIN SOLUTION NO PROMPT
    def __str__(self):
        """
        Return recently read contents; current element marked with >>.

        The __str__ method prints all tokens read so far, up to the end of the
        current line, and marks the current token with >>.
        """
        # Format string for right-justified line numbers
        n = len(self.lines)
        msg = '{0:>' + str(math.floor(math.log10(n)) + 1) + "}: "

        # Up to three previous lines and current line are included in output
        s = ''
        for i in range(max(0, n - 4), n - 1):
            s += msg.format(i + 1) + ' '.join(map(str, self.lines[i])) + '\n'
        s += msg.format(n)
        s += ' '.join(map(str, self.current_line))
        s += ' >> '
        s += ' '.join(map(str, self.current_line))
        return s.strip()
    # END SOLUTION


# Try to import readline for interactive history
try:
    import readline
except:
    pass


class InputReader:
    """An InputReader is an iterable that prompts the user for input."""

    def __init__(self, prompt):
        self.prompt = prompt

    def __iter__(self):
        while True:
            yield input(self.prompt)
            self.prompt = ' ' * len(self.prompt)


class LineReader:
    """A LineReader is an iterable that prints lines after a prompt."""

    def __init__(self, lines, prompt, comment=";"):
        self.lines = lines
        self.prompt = prompt
        self.comment = comment

    def __iter__(self):
        while self.lines:
            line = self.lines.pop(0).strip('\n')
            if (self.prompt is not None and line != "" and
                not line.lstrip().startswith(self.comment)):
                print(self.prompt + line)
                self.prompt = ' ' * len(self.prompt)
            yield line
        raise EOFError
