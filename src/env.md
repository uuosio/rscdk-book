# Setup Development Environment

## Setup Development Environment

### Install Rust

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Press enter when you see the following output:

```
Current installation options:


   default host triple: x86_64-apple-darwin
     default toolchain: stable (default)
               profile: default
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
```

Open a new terminal, run the following command to switch rust to nightly

```bash
rustup default nightly
```

### Install rust-src

```
rustup component add rust-src --toolchain nightly-x86_64-apple-darwin
```

### Install Rust Smart Contracts builder

```
cargo install --git=https://github.com/uuosio/cargo-eosiocontract --branch=eosio
```

That's all. See the next chapter on how to write a simple Smart Contracts and Build it.
