# Update
You can get features from the public repo by doing a pull request from the base repo.

# Deploy

Manual for now.  remember to upgrade version

export version=v1.0.0
docker build . -t eu.gcr.io/akbm-infrastructure/mssql-to-bq:${version}
docker push eu.gcr.io/akbm-infrastructure/mssql-to-bq:${version}
