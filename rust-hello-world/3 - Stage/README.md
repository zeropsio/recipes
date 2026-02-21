# Rust Hello World - Stage
This is staging environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=stage) recipe on [Zerops](https://zerops.io).

<!-- #ZEROPS_EXTRACT_START:intro# -->
Actix Web application connected to PostgreSQL, running as a pre-production staging environment on a single container using the same production build pipeline (`cargo build --release --locked`) to validate that release binaries and the readiness check work correctly before promotion.
<!-- #ZEROPS_EXTRACT_END:intro# -->
