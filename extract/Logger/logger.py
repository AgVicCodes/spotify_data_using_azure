import logging

class Logger:

    logging.basicConfig(
        filename = "app.log",
        level = logging.DEBUG,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(console_handler)