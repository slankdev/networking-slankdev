# networking-slankdev

## install
```
cd /opt/stack
git clone https://github.com/slankdev/networking-slankdev
sudo pip install -e ./
```

## Create test network
```
openstack network create --provider-network-type slankdev slankdev-net0
openstack subnet create slankdev-net0-subnet0 --dhcp --subnet-range 10.99.0.0/24 --network slankdev-net0
openstack port create slankdev-port0 --network slankdev-net0
openstack port set slankdev-port0 --binding-profile '{"slankdev": "hiroki shirokura", "asn":65000 }'
openstack port show -f json slankdev-port0
{
  "admin_state_up": true,
  "allowed_address_pairs": [],
  "binding_host_id": "",
  "binding_profile": {
    "slankdev": "hiroki shirokura",
    "asn": 65000
  },
  "binding_vif_details": {},
  "binding_vif_type": "unbound",
  "binding_vnic_type": "normal",
  "created_at": "2020-09-22T04:13:57Z",
  "data_plane_status": null,
  "description": "",
  "device_id": "",
  "device_owner": "",
  "dns_assignment": null,
  "dns_domain": null,
  "dns_name": null,
  "extra_dhcp_opts": [],
  "fixed_ips": [
    {
      "subnet_id": "edff4d43-9ed8-41dc-8f05-e1acebdb8220",
      "ip_address": "10.99.0.49"
    }
  ],
  "id": "337fb2f8-9a90-40e1-a1d6-79de0b9daac6",
  "ip_allocation": null,
  "mac_address": "fa:16:3e:b2:82:b1",
  "name": "slankdev-port0",
  "network_id": "d6a86933-d0f8-4263-82d1-32a25c11177f",
  "numa_affinity_policy": null,
  "port_security_enabled": true,
  "project_id": "60834db4e9f249a08e5391ac647498a6",
  "propagate_uplink_status": null,
  "qos_network_policy_id": null,
  "qos_policy_id": null,
  "resource_request": null,
  "revision_number": 3,
  "security_group_ids": [
    "eae88e63-ad49-4c88-962c-7db10b88ecad"
  ],
  "status": "DOWN",
  "tags": [],
  "trunk_details": null,
  "updated_at": "2020-09-22T04:20:57Z"
}
```

## References

- https://github.com/momijiame/openstack-neutron-ml2-dummy-driver
- https://github.com/line/networking-sr
