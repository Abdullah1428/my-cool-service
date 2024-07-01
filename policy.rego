package example.authz

default allow = false

allow {
    input.role == "admin"
    input.method == "POST"
}

allow {
    input.role == "admin"
    input.method == "GET"
}

allow {
    input.role == "user"
    input.method == "GET"
}
