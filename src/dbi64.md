# DBI64

```rust
pub struct DBI64<T>
where 
    T: Packer + PrimaryValueInterface + Default,
{
    ///
    pub code: u64,
    ///
    pub scope: u64,
    ///
    pub table: u64,
    _marker: core::marker::PhantomData<T>,
}
```

`DBI64` represents an on-chain key-value database with `u64` as key and store variable length of data.

## New

```rust
pub fn new(code: Name, scope: Name, table: Name) -> Self
```

Creates a new DBI64 instance

# Store

```rust
pub fn store(&self, key: u64,  value: &T, payer: Name) -> Iterator<T>
```

Store a value indexes by `key`. `payer` specifies account to pay the RAM resources.
VM throws an exception which can't catch by contract code if there is already a value with `key` exists in the database.

The following example code shows how to check if a value with the `key` already exists.

## Find

```rust
pub fn find(&self, key: u64) -> Iterator<T>
```

Find value by primary key

## Update

```rust
pub fn update(&self, iterator: &Iterator<T>, value: &T, payer: u64)
```

Update a value in database.
`payer` specifies account to pay the RAM resources. 
The related action in transaction must contain a corresponding permission of `payer`.


```rust
let it = db.find(key);
if !it.is_ok() {
    //create a new value
    //let value = ...
    db.store(key, &value, payer);
} else {
    let mut value = it.get_value();
    // modify value
    // ...
    db.update(it, &value, payer);
}
```

## Examples

[counter](https://github.com/uuosio/rscdk/blob/main/examples/counter/lib.rs)

[token](https://github.com/uuosio/rscdk/blob/main/examples/token/lib.rs)

## Source Code
[db.rs](https://github.com/uuosio/rscdk/blob/main/crates/eosio-chain/src/db.rs#L442)
