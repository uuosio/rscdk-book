# Name

## name macro

Usage:
```rust
    let contract_name = name!("hello");
```

This macro is a convenient way to creates a `Name` instance. 

## new

```rust
pub fn new(s: &'static str) -> Self
```

Creates a new Name struct instance. This method accept `static` `&str` as it's parameter.

This method convert a name represent in string to a `u64` value.

For using `&str` to create a Name instance, use `Name::from_str`.

`s` normally is a `&'static str` that has up to 12 characters with each character in the range of [a-z1-5].

It can have up to 13 characters with the lastest character in the range of [1-5a-j].

## value

```rust
pub fn value(&self) -> u64
```

Get the `u64` value of the Name

## from_u64

```rust
pub fn from_u64(n: u64) -> Self
```

Creates an Name instance from `u64`

## from_str
```rust
pub fn from_str(s: &str) -> Self
```

Creates an Name instance from `&str`

## to_string
```rust
pub fn to_string(&self) -> String
```

Convert a name to `String` representation

## Source Code
[name.rs](https://github.com/uuosio/rscdk/blob/main/crates/eosio-chain/src/name.rs)
