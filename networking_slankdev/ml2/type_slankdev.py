from neutron_lib import exceptions as exc
from neutron_lib.plugins.ml2 import api
from oslo_log import log

from neutron._i18n import _

LOG = log.getLogger(__name__)
TYPE_NAME = "slankdev"


class SlankdevTypeDriver(api.ML2TypeDriver):
    """
    Manage state for slankdev networks with ML2.
    The SlankdevTypeDriver implements the 'slankdev' network_type.
    """

    def __init__(self):
        super(SlankdevTypeDriver, self).__init__()

    def get_type(self):
        return TYPE_NAME

    def initialize(self):
        LOG.info("ML2 SlankdevTypeDriver initialization complete")

    def is_partial_segment(self, segment):
        return False

    def validate_provider_segment(self, segment):
        for key, value in segment.items():
            if value and key not in [api.NETWORK_TYPE]:
                msg = _("%s prohibited for slankdev provider network") % key
                raise exc.InvalidInput(error_message=msg)

    def reserve_provider_segment(self, context, segment, filters=None):
        return segment

    def allocate_tenant_segment(self, context, filters=None):
        return

    def release_segment(self, context, segment):
        pass

    def get_mtu(self, physical_network=None):
        pass

    def initialize_network_segment_range_support(self):
        pass

    def update_network_segment_range_allocations(self):
        pass
