import sys
import time
from oslo_config import cfg
from oslo_log import log as logging
from neutron.common import config as common_config

LOG = logging.getLogger(__name__)


def main():
    common_config.init(sys.argv[1:])
    common_config.setup_logging()

    #manager = SlankdevManager()
    polling_interval = cfg.CONF.AGENT.polling_interval
    quitting_rpc_timeout = cfg.CONF.AGENT.quitting_rpc_timeout
    LOG.info("SLANKDEV_AGENT")
    LOG.info("ohgeadlfjldksfadl to exti")
    sys.exit(1)
    while True:
        LOG.info("SLANKDEV_AGENT")
        time.sleep(1)
