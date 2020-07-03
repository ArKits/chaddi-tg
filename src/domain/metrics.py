from prometheus_client import start_http_server, Counter
from util import config, util
from loguru import logger

# Get application config
chaddi_config = config.get_config()


message_counter = Counter("chaddi_messages_count", "chaddi_messages_count")


def serve_metrics():
    logger.info("Serving Metrics on port={}", chaddi_config["metrics"]["port"])
    start_http_server(chaddi_config["metrics"]["port"])
    return


def inc_message_count():
    message_counter.inc()
    return
