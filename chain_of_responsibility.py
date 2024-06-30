class Logger:
    def __init__(self, next_logger=None):
        self._next_logger = next_logger

    def log_message(self, level, message):
        if self._next_logger:
            self._next_logger.log_message(level, message)


# Concrete Handlers
class InfoLogger(Logger):
    def log_message(self, level, message):
        if level == "INFO":
            print(f"INFO: {message}")
        else:
            super().log_message(level, message)


class DebugLogger(Logger):
    def log_message(self, level, message):
        if level == "DEBUG":
            print(f"DEBUG: {message}")
        else:
            super().log_message(level, message)


class ErrorLogger(Logger):
    def log_message(self, level, message):
        if level == "ERROR":
            print(f"ERROR: {message}")
        else:
            super().log_message(level, message)


# Client Code
if __name__ == "__main__":
    # Create the chain of loggers
    error_logger = ErrorLogger()
    debug_logger = DebugLogger(error_logger)
    info_logger = InfoLogger(debug_logger)

    # Log messages with different levels
    info_logger.log_message("INFO", "This is an informational message.")
    info_logger.log_message("DEBUG", "This is a debug message.")
    info_logger.log_message("ERROR", "This is an error message.")
    info_logger.log_message("INFO", "Another informational message.")
    list = list(map(str, input().split(" ")))
    print(list)
