<!-- #ZEROPS_REMOVE_START# -->
# ELK — Production Environment
This is a production environment for [ELK (info + deploy)](https://app.zerops.io/recipes/elk?environment=production) recipe on [Zerops](https://zerops.io).
<!-- #ZEROPS_REMOVE_END# -->

<!-- #ZEROPS_REMOVE_START# -->
<!-- #ZEROPS_EXTRACT_START:intro# -->
**Production** environment provides a production-ready ELK setup with highly-available Elasticsearch storage.
<!-- #ZEROPS_EXTRACT_END:intro# -->

# Takeover and Maintenance Guide
<!-- #ZEROPS_REMOVE_END# -->

> [!TIP]
> To play around with settings, scaling and upgrades effectively,
> it proved successful for us - the maintainers of this recipe -
> to use the following or similar workflow (demonstrating on Kibana service):
>
> 1. enter "Remote Terminal" in GUI or [login via SSH](https://docs.zerops.io/references/networking/ssh)
> 2. `sudo su` to gain permission for editing `kibana`'s files
> 3. fiddle with settings in `/etc/kibana/`
> 4. `systemctl restart kibana`
> 5. `journalctl -f -u kibana` to see what's happening
>
> Another useful tip is temporarily disabling the `deploy.readinessCheck` in `zerops.yaml`,
> allowing to tweak and finalize the unsuccessful deployments at runtime, and permeating the changes into `zerops.yaml` after.

## Scaling

### Elasticsearch

_TBD: Currently, Zerops only supports two operating modes (single-node, 3-node), without direct support for upgrading between them. Different modes and machine-managed upgrades are coming soon._

### Kibana

Scaling Kibana instances horizontally (adding more containers) is theoretically possible, but it requires more complex setup. For more information see: https://www.elastic.co/docs/deploy-manage/production-guidance/kibana-load-balance-traffic

### Logstash and APM Server

Logstash and AMP server allows for horizontal scaling, simply increase minimum number of containers in the "Automatic Scaling Configuration" menu.
For more information visit the individual apps README's below.

## Upgrades

> [!CAUTION]
> Please refer to the https://www.elastic.co/support/matrix#matrix_compatibility and https://www.elastic.co/guide/en/kibana/8.19/upgrade.html before you proceed with upgrades.

Upgrades are done by upgrading the Elasticsearch storage service (_TBD, please refer to the "Scaling > Elasticsearch" of this manual_)
and manipulating the installed versions in the `run.prepareCommands` section of `zerops.yaml`s of the individual apps ([Kibana](https://github.com/zerops-recipe-apps/elk-kibana-app), [Logstash](https://github.com/zerops-recipe-apps/elk-logstash-app), ...).
This can be done by forking the app repository and/or `zcli push` with the changed `zerops.yaml`.

## Data Management

Automatic encrypted backups are enabled by default for the Elasticsearch service.
The backup format is of the [elasticdump](https://github.com/elasticsearch-dump/elasticsearch-dump) utility (i.e. output of this command `elasticdump --input=http://localhost:9200 --output=$ --limit=100`).
Feel free to enable snapshots by adding Object Storage service, see "Scaling > Elasticsearch".
