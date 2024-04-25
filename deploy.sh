#!/bin/sh

# Deploy the DWH project to the server

minikube kubectl delete -- -f kube_files/services/

minikube kubectl delete -- -f kube_files/deployments/

minikube kubectl delete -- -f kube_files/configs/

minikube kubectl apply -- -f kube_files/configs/

minikube kubectl apply -- -f kube_files/deployments/

minikube kubectl apply -- -f kube_files/services/