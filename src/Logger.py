import logging

def setMode(mode):
    time_format = '%Y-%m-%d %I:%M:%S %p'
    time_formatter = logging.Formatter(fmt='%(asctime)s - [%(levelname)s] :: %(message)s', datefmt=time_format)
    logger = logging.getLogger()
        
    if mode == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif mode == "INFO":
        logger.setLevel(logging.INFO)
    else:
        raise ValueError("Invalid mode. Mode must be either 'DEBUG' or 'INFO'.")

    handler = logging.StreamHandler()
    handler.setFormatter(time_formatter)
    logger.addHandler(handler)
    return