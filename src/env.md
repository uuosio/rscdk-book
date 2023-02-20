# Setup Development Environment

## Install Rust

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
```

Activate the new PATH environment.

```bash
source $HOME/.cargo/env
```

## Install Nightly Rust

```bash
rustup toolchain install nightly --component rust-src
```

## Install binaryen

* Install `binaryen` in a version >= 99:
  * [Debian/Ubuntu](https://tracker.debian.org/pkg/binaryen): `apt-get install binaryen`
  * [Homebrew](https://formulae.brew.sh/formula/binaryen): `brew install binaryen`
  * [Arch Linux](https://archlinux.org/packages/community/x86_64/binaryen/): `pacman -S binaryen`
  * Windows: [binary releases are available](https://github.com/WebAssembly/binaryen/releases)

## Create a Virtual Python Env for Testing
```bash
python3 -m venv ~/env
source ~/env/bin/activate
python3 -m pip install --upgrade pip
```

Next time you want to use the test environment, just run the following command again.

```
source ~/env/bin/activate
```

## Install Eos Test Framework

```
python3 -m pip install ipyeos
```

## Install Rust Smart Contracts Builder 

```
python3 -m pip install rust-contracts-builder
```

## Install Python Toolkit for EOS 

```bash
python3 -m pip install pyeoskit
```

pyeoskit is used to deploy contracts.

## Checking Environment

Create a new rust contract project:

```bash
rust-contract init hello
```

Build

```bash
cd hello
./build.sh
```

Test

```bash
cargo test
```

If `eosdebugger` is running, it will output information like the following:

```bash
debug 2023-02-20T07:03:09.852 ipyeos    controller.cpp:2406           clear_expired_input_ ] removed 0 expired transactions of the 41 input dedup list
debug 2023-02-20T07:03:09.861 ipyeos    controller.cpp:2406           clear_expired_input_ ] removed 0 expired transactions of the 47 input dedup list
debug 2023-02-20T07:03:09.887 ipyeos    controller.cpp:2406           clear_expired_input_ ] removed 0 expired transactions of the 49 input dedup list
debug 2023-02-20T07:03:09.891 ipyeos    apply_context.cpp:28          print_debug          ]
[(hello,inc)->hello]: CONSOLE OUTPUT BEGIN =====================
count is 1

[(hello,inc)->hello]: CONSOLE OUTPUT END   =====================
debug 2023-02-20T07:03:09.894 ipyeos    controller.cpp:2406           clear_expired_input_ ] removed 0 expired transactions of the 50 input dedup list
debug 2023-02-20T07:03:09.897 ipyeos    apply_context.cpp:28          print_debug          ]
[(hello,inc)->hello]: CONSOLE OUTPUT BEGIN =====================
count is 2

[(hello,inc)->hello]: CONSOLE OUTPUT END   =====================
debug 2023-02-20T07:03:09.899 ipyeos    controller.cpp:2406           clear_expired_input_ ] removed 0 expired transactions of the 51 input dedup list
Listening for new connection...
```

In addition, you can use the `test.sh` script to run tests, eliminating the need for `eosdebugger` to be running.
```bash
./test.sh
```

If you see the following output, that means everything have been installed successfully.

```
test.py debug 2022-07-04T04:01:58.496 ipyeos    apply_context.cpp:36          print_debug          ] 
[(hello,inc)->hello]: CONSOLE OUTPUT BEGIN =====================
count is 1

[(hello,inc)->hello]: CONSOLE OUTPUT END   =====================
debug 2022-07-04T04:01:58.498 ipyeos    apply_context.cpp:36          print_debug          ] 
[(hello,inc)->hello]: CONSOLE OUTPUT BEGIN =====================
count is 2

[(hello,inc)->hello]: CONSOLE OUTPUT END   =====================
.

============================== 1 passed in 0.90s ===============================
```
