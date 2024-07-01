# My Cool Service

## Overview

This service provides very simple two REST endpoints.

- GET - https://my-cool-service:8000/api/users
  - a. Any authenticated user can read users.
  - b. The endpoint returns list of users as JSON
  - c. User attributes: name, email
- POST - https://my-cool-service:8000/api/users
  - a. Only "admin" role can create new users.
  - b. User attributes: name, email

## App Structure

- `app/`: Contains user-related API logic.
- `app/routes/`: Contains the user routes
- `app/services/`: Contains OPA integration for authorization.
- `app/utils`: Contains utils for example logger
- `k8s/`: Kubernetes deployment and service definitions.
- `tests/`: Contains simple tests for the app
- `policy.rego`: OPA policy for authorization.

## SETUP Guide

## Prerequisites

- Docker
- kubectl
- Minikube

Ensure Docker, kubectl, and Minikube (or a similar Kubernetes setup) are installed on the target machine.

### Start Minikube and set env to local

```
minikube start --driver=docker

eval $(minikube docker-env)
```

### Build the Docker Image

```
docker build -t my-cool-service:latest .
```

### Deployment

```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/opa-configmap.yaml
kubectl apply -f k8s/opa-deployment.yaml
```

### Testing on localhost with Port Forwarding

```
kubectl port-forward service/my-cool-service 8000:8000 &
kubectl port-forward service/opa 8181:8181 &
```

### Restarting after making changes

```
kubectl rollout restart deployment "service_name"
kubectl rollout restart deployment opa
kubectl rollout restart deployment my-cool-service
```

### Testing

- GET /api/users with Role: user should succeed.
- POST /api/users with Role: admin should succeed.
- Unauthorized roles should receive 403.

Send the following requests from your terminal or use any testing tool

#### Authorized GET request (user role)
curl -H "Role: user" -X GET http://localhost:8000/api/users

#### Unauthorized POST request (user role)
curl -H "Content-Type: application/json" -H "Role: user" -X POST -d '{"name": "user3", "email": "user3@example.com"}' http://localhost:8000/api/users

#### Authorized GET request (admin role)
curl -H "Role: admin" -X GET http://localhost:8000/api/users

#### Authorized POST request (admin role)
curl -H "Content-Type: application/json" -H "Role: admin" -X POST -d '{"name": "user3", "email": "user3@example.com"}' http://localhost:8000/api/users


## Improvements Needed

This app can be improved alot in terms of code refactoring, software dev practices, security practices but due to time constraint could not be possible for now.

Some things that needs to be added

- Ingress integration so that this services can acutally be available to external browsers, currently this uses port forwarding locally to test the app
- Write units test, coverage tests
- Better code structure