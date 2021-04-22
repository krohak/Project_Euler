class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.digest = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.digest and timestamp < self.digest[message]+10:
            return False
        self.digest[message] = timestamp
        return True