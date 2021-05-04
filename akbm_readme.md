# Update
You can get features from the public repo by doing a pull request from the base repo.

# Deploy

Manual for now.  remember to upgrade version

export version=v1.0.5
docker build . -t eu.gcr.io/akbm-infrastructure/mssql-to-bq:${version}
docker push eu.gcr.io/akbm-infrastructure/mssql-to-bq:${version}

# Config.yaml template and secret template
Note that the first three dashes are important.
```yaml
---
  db_username: the_username
  db_password: the_password
  db_host: 127.0.0.1
  db_database: thedb
```

# SM secrets tutorial
First make sure you can create and access secrets, or have a SA that can do it.
## To Get the SECRETMANAGER_URI
- To to cloud console
- https://console.cloud.google.com/security/secret-manager/secret/jeeves-db-credentials/versions?project=akbm-infrastructure
- click the three dots, copy resource id:
- For Jeeves this is: projects/483261958633/secrets/jeeves-db-credentials/versions/1

Set the SECRETMANAGER_URI environment variable to that value and you are good to go.

## Creating secrets
- secretmanager, clikc create secret
- in the "secret value" input the 5 lines from the template.  Replace values as needed.
- leave rest to default.