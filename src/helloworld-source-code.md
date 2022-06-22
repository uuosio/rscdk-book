# Source Code

Create a `helloworld` directory and save the following two files in it.

## lib.rs
```rust
#![cfg_attr(not(feature = "std"), no_std)]

#[eosio_chain::contract]
mod hello {
    use eosio_chain::{
        Name,
        eosio_println,
    };

    #[chain(main)]
    #[allow(dead_code)]
    pub struct Hello {
        receiver: Name,
        first_receiver: Name,
        action: Name,
    }

    impl Hello {

        pub fn new(receiver: Name, first_receiver: Name, action: Name) -> Self {
            Self {
                receiver: receiver,
                first_receiver: first_receiver,
                action: action,
            }
        }

        #[chain(action="sayhello")]
        pub fn say_hello(&self, name: String) {
            eosio_println!("++++hello", name);
        }
    }
}
```

## Cargo.toml

```ini
[package]
name = "helloworld"
version = "0.1.0"
authors = [""]
edition = "2021"

[dependencies]
eosio_chain = { version = "0.1.0", git = "https://github.com/uuosio/rscdk", default-features = false }

[lib]
name = "helloworld"
path = "lib.rs"
crate-type = ["cdylib", "rlib"]

[features]
default = ["std"]
std = [
    "eosio_chain/std",
]
```
