# Enabling in DevStack

1. Download DevStack
2. Use following `local.conf`.cA

```ini
[[local|localrc]]
ADMIN_PASSWORD=secret
DATABASE_PASSWORD=$ADMIN_PASSWORD
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD
LOGFILE=/opt/stack/logs/stack.sh.log

enable_plugin networking-slankdev https://github.com/slankdev/networking-slankdev master

[[post-config|$Q_PLUGIN_CONF_FILE]]
[ml2]
tenant_network_types=slankdev
type_drivers=slankdev
mechanism_drivers=slankdev
```

3. Run stack.sh
