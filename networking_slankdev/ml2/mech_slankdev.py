from oslo_log import log
from neutron.plugins.ml2.drivers import mech_agent
from networking_slankdev.ml2 import type_slankdev

LOG = log.getLogger(__name__)


class SlankdevMechanismDriver(mech_agent.SimpleAgentMechanismDriverBase):

    def __init__(self):
        pass

    def get_allowed_network_types(self, agent=None):
        return [type_slankdev.TYPE_NAME]

    def get_mappings(self, agent):
        pass

    def initialize(self):
        pass

    def create_network_precommit(self, context):
        pass

    def create_network_postcommit(self, context):
        pass

    def update_network_precommit(self, context):
        pass

    def update_network_postcommit(self, context):
        pass

    def delete_network_precommit(self, context):
        pass

    def delete_network_postcommit(self, context):
        pass

    def create_subnet_precommit(self, context):
        pass

    def create_subnet_postcommit(self, context):
        pass

    def update_subnet_precommit(self, context):
        pass

    def update_subnet_postcommit(self, context):
        pass

    def delete_subnet_precommit(self, context):
        pass

    def delete_subnet_postcommit(self, context):
        pass

    def create_port_precommit(self, context):
        pass

    def create_port_postcommit(self, context):
        pass

    def update_port_precommit(self, context):
        LOG.info("SLANKDEV UPDATE PORT PRECOMMIT")
        pass

    def update_port_postcommit(self, context):
        LOG.info("SLANKDEV UPDATE PORT POSTCOMMIT")
        pass

    def delete_port_precommit(self, context):
        pass

    def delete_port_postcommit(self, context):
        pass

    def bind_port(self, context):
        pass
