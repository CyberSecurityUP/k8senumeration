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

### Configure EKS

AWS Configure Key
`
aws configure
`

AWS Authentication Info
`
aws sts get-caller-identity
`

AWS Kube Configuration
`
aws eks update-kubeconfig --name cluster-name1 --region us-east-1
aws eks update-kubeconfig --name cluster-name2 --region us-east-1
`


## Using K8SEnumeration

### Running Tool

`
python3 k8senumgcp.py
`



