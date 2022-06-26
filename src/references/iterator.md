# Iterator

```rust
pub struct Iterator<'a, T> 
where T: Packer + PrimaryValueInterface + Default
{
    ///
    pub(crate) i: i32,
    pub(crate) primary: Option<u64>,
    db: &'a DBI64<T>,
}
```

## get_primary

```rust
pub fn get_primary(&self) -> Option<u64>
```

Get primary key of iterator

access `DBI64` to extract primary key from value if primary key is not cached

## get_value

```rust
pub fn get_value(&self) -> Option<T>
```

Get database value by iterator

## get_i

```rust
pub fn get_i(&self) -> i32
```

Get the raw iterator value

## is_ok

```rust
pub fn is_ok(&self) -> bool
```

return `true` if iterator is valid, else `false`

## is_end

```rust
pub fn is_end(&self) -> bool
```

return `true` if it's a valid end iterator, else `false`

use this method to check the return value of `MultiIndex.end` or `DBI64.end`

## expect

```rust
pub fn expect(self, msg: &str) -> Self
```

help function for asserting.


Example:

```rust
db.find(1).expect("invalid iterator");
```

## expect_not_ok

```rust
pub fn expect_not_ok(self, msg: &str) -> Self
```

help function for asserting.

## Source Code
[db.rs](https://github.com/uuosio/rscdk/blob/main/crates/eosio-chain/src/db.rs#L308)
