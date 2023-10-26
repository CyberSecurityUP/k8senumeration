# k8senumgcp
Kubernetes, Clusters and Dockers Enumeration in GCP and AWS environments 

## Install kubectl in GCP


### Install kubectl component in gcloud:

`
gcloud components install kubectl
`


### Check if kubectl is installed:

`
kubectl version
`

### Install authentication k8s Plugin

`
gke-gcloud-auth-plugin --version
`

### Update kubectl configuration to use the plugin:

`
gcloud container clusters get-credentials CLUSTER_NAME \
    --region=COMPUTE_REGION
`

## Using K8SEnum

`
python3 k8senumgcp.py
`



