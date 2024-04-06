import functools
from datetime import datetime

def log_execution_to_file(file_path):
    def decorator_log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if args:
                class_name = ''
                if hasattr(args[0], '__class__'):
                    class_name = args[0].__class__.__name__
                elif hasattr(func, '__self__') and hasattr(func.__self__, '__class__'):
                    class_name = func.__self__.__class__.__name__

                with open(file_path, "a") as f:
                    f.write(f"[{current_time}] Class: {class_name} - Function: {func.__name__} \n")
            else:
                with open(file_path, "a") as f:
                    f.write(f"[{current_time}] Function: {func.__name__}\n")

            return result
        return wrapper
    return decorator_log