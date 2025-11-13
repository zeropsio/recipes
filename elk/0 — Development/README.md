<!-- #ZEROPS_REMOVE_START# -->
# Bun Hello World — Small Production Environment
This is a small production environment for [Bun Hello World (info + deploy)](https://app.zerops.io/recipes/bun-hello-world?environment=stage) recipe on [Zerops](https://zerops.io).
<!-- #ZEROPS_REMOVE_END# -->

<!-- #ZEROPS_REMOVE_START# -->
<!-- #ZEROPS_EXTRACT_START:intro# -->
**Development** environment provides a low-resource ELK setup, suitable for small productions or development.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide
<!-- #ZEROPS_REMOVE_END# -->

<!-- #ZEROPS_EXTRACT_START:maintenance_guide# -->
## Scaling

### Elasticsearch (storage)

_TBD: Currently, Zerops only supports two operating modes (single-node, 3-node), without direct support for upgrading between. Different modes and machine-managed upgrades are coming soon._

If you wish to upgrade to highly-available 3-node setup, follow these instructions:

1. export as YAML and delete the stateless `kibana`, `logstash` and `apmserver` services
2. create a backup of `elkstorage` service (from the GUI)
3. download the backup
4. install the [elasticsearch-dump](https://github.com/elasticsearch-dump/elasticsearch-dump) utility
5. delete the current `elkstorage` service
6. create new `elkstorage` Elasticsearch service with the same version but with `HA` mode
7. connect to the project [via zCLI VPN](https://docs.zerops.io/references/networking/vpn)
8. insert the backup data to the new `elkstorage` service
    ```bash
    elasticdump --input=/path/to/downloaded/backup-file --output=http://elastic:$ELASTIC_PASSWORD_FROM_GUI@elkstorage:9200 --limit 1000
    ```
9. re-import the stateless ELK services (`kibana`, `logstash`, `apmserver`)

> [!NOTE]
> If you are willing to lose your logs, traces and settings, feel free to skip steps 2,3,4,7,8. 

### Kibana

Scaling Kibana instances horizontally is theoretically possible, for more information see: https://www.elastic.co/docs/deploy-manage/production-guidance/kibana-load-balance-traffic

### Logstash

Logstash allows for horizontal scaling, simply increase minimum number of containers.

### APM Server

AMP server allows for horizontal scaling, simply increase minimum number of containers.

## Upgrades

Please refer to the https://www.elastic.co/support/matrix#matrix_compatibility and https://www.elastic.co/guide/en/kibana/8.19/upgrade.html.

## Data Management

About data management.

_TODO: Complete this._
<!-- #ZEROPS_EXTRACT_END:maintenance_guide# -->
