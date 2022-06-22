## Generating an ABI File for a Smart Contract

ABI(Application Binary Interface) provides a way to interact with contracts

First create a directory named `abigen` subdirectory. Then save the following two files in it.

### Cargo.toml

```ini
[package]
authors = [""]
edition = "2021"
name = "abi-gen"
publish = false
rust-version = "1.56.1"
version = "0.1.0"

[[bin]]
name = "abi-gen"
path = "main.rs"

[dependencies]

[dependencies.contract]
package = "helloworld"
path = ".."

[features]
default = ["std"]
std = [
]
```

### main.rs

```rust
use std::{fs, path::Path};
extern crate contract;

extern "Rust" {
	pub fn __eosio_generate_abi() -> String;
}

fn main() -> Result<(), std::io::Error> {
	let abi = unsafe {
		__eosio_generate_abi()
	};

	fs::write(Path::new("./target/helloworld.abi"), abi)?;
	Ok(())
}
```

### Generating an ABI file

In `abigen` directory, run the following command to generating an ABI file:

```bash
cargo run --package abi-gen --release
```
