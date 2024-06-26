#!/usr/bin/bash
export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=python-rest-api,app.kubernetes.io/instance=python-rest-api-chart" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
echo "Use http://127.0.0.1:8080 to use your application"
kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT