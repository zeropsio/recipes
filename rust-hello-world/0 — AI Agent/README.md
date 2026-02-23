<!-- #ZEROPS_EXTRACT_START:intro# -->
# Rust Hello World - AI Agent
This is an AI agent development environment for [Rust Hello World (info + deploy)](https://app.zerops.io/recipes/rust-hello-world?environment=ai-agent) recipe on [Zerops](https://zerops.io).

Two services are deployed: `appdev` running the `dev` setup (full source tree with pre-fetched crates, idle container ready for SSH), and `appstage` running the `prod` setup (compiled release binaries) for pipeline validation — both connected to a shared PostgreSQL database.
<!-- #ZEROPS_EXTRACT_END:intro# -->
