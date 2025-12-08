import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {args if args else 'none'}")
        logger.info(f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.info(f"return: {result}")
        logger.info("-----")
        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def many_positional_args(*args):
    return True

@logger_decorator
def many_keyword_args(**kwargs):
    return logger_decorator   

if __name__ == "__main__":
    hello_world()
    many_positional_args(1, 2, 3, 4, 5)
    many_keyword_args(name="Chandana", age=26, job="Engineer")
