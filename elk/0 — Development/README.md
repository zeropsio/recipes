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

_TBD: Currently, Zerops only supports two operating modes (single-node, 3-node), without direct support for upgrading between them. Different modes and machine-managed upgrades are coming soon._

If you wish to upgrade to highly-available 3-node setup, follow these instruction:

1. stop the `kibana`, `logstash` and `apmserver` services
2. create an Object Storage service `elksnapshots` with sufficient size and `private` access
3. copy secrets from `elksnapshots` > "Access Details" and set them as environment variable of `elkstorage` service

    ```shell
    S3_ACCESS_KEY=<copied-access-key-id>
    S3_SECRET_KEY=<copied-secret-key>
    ```

4. restart the `elkstorage` service (to reflect the `S3_ACCESS_KEY` and `S3_SECRET_KEY` environment variables)
5. connect to the project via [zCLI VPN](https://docs.zerops.io/references/networking/vpn)
6. register snapshot repository and create snapshot

    Export variables:
    ```bash
    export ELASTIC_PASSWORD=<copied-elastic-password>
    export S3_BUCKET=<copied-object-storage-bucket>
    ```

    Check that you can connect to the Elasticsearch:
    ```bash
    curl "http://elkstorage:9200?pretty" \
    -u "elastic:$ELASTIC_PASSWORD"
    ```
    
    Set up the snapshot repository:
    ```bash
    curl -X PUT "http://elkstorage:9200/_snapshot/s3_backup?pretty" \
    -H "Content-Type: application/json" \
    -u "elastic:$ELASTIC_PASSWORD" \
    -d "{
      \"type\": \"s3\",
      \"settings\": {
        \"bucket\": \"$S3_BUCKET\",
        \"client\": \"default\",
        \"endpoint\": \"storage-prg1.zerops.io\",
        \"protocol\": \"https\",
        \"path_style_access\": true,
        \"base_path\": \"snapshots\"
      }
    }"
    ```
    
    Make a snapshot:
    ```bash
    curl -X PUT "http://elkstorage:9200/_snapshot/s3_backup/snapshot_1?pretty" \
    -u "elastic:$ELASTIC_PASSWORD"
    ```
    
    Check that snapshot was created and is listed:
    ```bash
    curl "http://elkstorage:9200/_snapshot/s3_backup/_all?pretty" \
    -u "elastic:$ELASTIC_PASSWORD"
    ```

    > [!TIP]
    > More information about registering S3 snapshot repository or creating backups are here:
    > https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/s3-repository
    > https://www.elastic.co/docs/deploy-manage/tools/snapshot-and-restore/create-snapshots#manually-create-snapshot

7. delete the current `elkstorage` service
8. create a new `elkstorage` service with `mode: HA` and set S3 access secrets as environment variables

    ```shell
    S3_ACCESS_KEY=<copied-access-key-id>
    S3_SECRET_KEY=<copied-secret-key>
    ```

9. restart the `elkstorage` service
10. restore the snapshot

    Re-export the password variable:
    ```bash
    export ELASTIC_PASSWORD=<copied-elastic-password-of-the-new-elkstorage>
    ```

    Check that you can connect to the new Elasticsearch:
    ```bash
    curl "http://elkstorage:9200?pretty" \
    -u "elastic:$ELASTIC_PASSWORD"
    ```

    Allow wildcard deletion of indices:
    ```bash
    curl -X PUT "http://elkstorage:9200/_cluster/settings?pretty" \
    -H "Content-Type: application/json" \
    -u "elastic:$ELASTIC_PASSWORD" \
    -d '{
      "persistent": {
        "action.destructive_requires_name": false
      }
    }' 
    ```
    
    Delete all indices and data streams, except `.security`:
    ```bash
    curl -X DELETE "http://elkstorage:9200/_data_stream/*,-.security*?expand_wildcards=all&pretty" \
    -u "elastic:$ELASTIC_PASSWORD"
    curl -X DELETE "http://elkstorage:9200/*,-.security*?expand_wildcards=all&pretty" \
    -u "elastic:$ELASTIC_PASSWORD"
    ```
    
    Set up the snapshot repository:
    ```bash
    curl -X PUT "http://elkstorage:9200/_snapshot/s3_backup?pretty" \
    -H "Content-Type: application/json" \
    -u "elastic:$ELASTIC_PASSWORD" \
    -d "{
      \"type\": \"s3\",
      \"settings\": {
        \"bucket\": \"$S3_BUCKET\",
        \"client\": \"default\",
        \"endpoint\": \"storage-prg1.zerops.io\",
        \"protocol\": \"https\",
        \"path_style_access\": true,
        \"base_path\": \"snapshots\"
      }
    }"
    ```
    
    Finally, restore from snapshot:
    ```bash
    curl "http://elkstorage:9200/_snapshot/s3_backup/snapshot_1/_restore?pretty" \
    -H "Content-Type: application/json" \
    -u "elastic:$ELASTIC_PASSWORD" \
    -d '{
        "indices": "*,-.security*",
        "feature_states": ["kibana"],
        "include_global_state": false,
        "include_aliases": true
    }'
    ```

    > [!NOTE]
    > Keeping the `.security` indices intact, as the newly created service has its own security settings.
    > Feel free to include more `feature_states` depending on your setup (e.g. `geoip`).

11. re-deploy the `kibana`, `logstash` and `apmserver` services
    
    In service left menu, go to "Pipelines & CI/CD settings" or navigate to `/service-stack/$ID/deploy` and click `Trigger re-deploy` button.
    This will cause the services to start with updated security settings.

Feel free to remove `elksnapshots` service and disable `action.destructive_requires_name` settings after the migration is complete.

### Kibana

Scaling Kibana instances horizontally (adding more containers) is theoretically possible, but it requires more complex setup. For more information see: https://www.elastic.co/docs/deploy-manage/production-guidance/kibana-load-balance-traffic

### Logstash and APM Server

Logstash and AMP server allows for horizontal scaling, simply increase minimum number of containers in the "Automatic Scaling Configuration" menu.

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

<!-- #ZEROPS_EXTRACT_END:maintenance_guide# -->
