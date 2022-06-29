# Setup Development Environment

## Install Rust

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

## Install rust-src

```
rustup component add rust-src --toolchain nightly-x86_64-apple-darwin
```

## Install Rust Smart Contracts Builder 

```
python3 -m pip install rust-contracts-builder
```

## Install binaryen

* Install `binaryen` in a version >= 99:
  * [Debian/Ubuntu](https://tracker.debian.org/pkg/binaryen): `apt-get install binaryen`
  * [Homebrew](https://formulae.brew.sh/formula/binaryen): `brew install binaryen`
  * [Arch Linux](https://archlinux.org/packages/community/x86_64/binaryen/): `pacman -S binaryen`
  * Windows: [binary releases are available](https://github.com/WebAssembly/binaryen/releases)

## Install Eos Test Framework

```
python3 -m venv ~/env
source ~/env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install ipyeos
```

Next time if you want to run tests in examples, you need to active virtual env again.

```
source ~/env/bin/activate
```

## Install Python Toolkit for EOS 

```bash
source ~/env/bin/activate
python3 -m pip install pyeoskit
```

pyeoskit is used to deploy a contract.
