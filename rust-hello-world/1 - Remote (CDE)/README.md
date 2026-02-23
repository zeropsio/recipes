# Rust Hello World - Remote (CDE)

<!-- #ZEROPS_EXTRACT_START:intro# -->
This is a remote development environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=remote-cde) recipe on [Zerops](https://zerops.io).

Two application containers and a PostgreSQL database: `appdev` (dev setup) provides a full Rust toolchain workspace accessible via SSH or cloud IDE mounting (VS Code Remote, Zed over SSHFS), while `appstage` (prod setup) allows testing the complete release build pipeline before promoting to production.
<!-- #ZEROPS_EXTRACT_END:intro# -->
