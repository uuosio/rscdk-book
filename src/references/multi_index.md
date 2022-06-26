# MultiIndex

## new

```rust
pub fn new(code: Name, scope: Name, table: Name, indexes: &[SecondaryType]) -> Self
```


## set

```rust
pub fn set(&self, key: u64, value: &T, payer: Name) -> Iterator<T>
```

## store

```rust
pub fn store(&self, value: &T, payer: Name) -> Iterator<T>
```

Store a value index by primary_key of `value`. `payer` specifies account to pay the RAM resources. Code execution fails if there is already a value with primary_key in the database. `store` method calls `value.get_primary()` to get primary key 

```rust
let it = db.find(key);
if !it.is_ok() {
    //create a new value
    //let value = ...
    db.store(&value, payer);
} else {
    let mut value = it.get_value();
    // modify value
    // ...
    db.update(it, &value, payer);
}
```

## update

```rust
pub fn update(&self, iterator: &Iterator<T>, value: &T, payer: Name)
```

Update a value in database. payer specifies account to pay the RAM resources. The related action in transaction must contain a corresponding permission of payer.

## remove

```rust
pub fn remove(&self, iterator: &Iterator<T>)
```

## get

```rust
pub fn get(&self, iterator: &Iterator<T>) -> Option<T>
```

## get_by_primary

```rust
pub fn get_by_primary(&self, primary: u64) -> Option<T>
```

## next

```rust
pub fn next(&self, iterator: &Iterator<T>) -> Iterator<T>
```

## previous

```rust
pub fn previous(&self, iterator: &Iterator<T>) -> Iterator<T>
```

## find

```rust
pub fn find(&self, id: u64) -> Iterator<T>
```

## lowerbound
```rust
pub fn lowerbound(&self, id: u64) -> Iterator<T>
```

## upperbound

```rust
pub fn upperbound(&self, id: u64) -> Iterator<T>
```

## end

```rust
pub fn end(&self) -> Iterator<T>
```

## get_idx_db

```rust
pub fn get_idx_db(&self, i: usize) -> &dyn IndexDB
```

## idx_update

```rust
pub fn idx_update(&self, it: SecondaryIterator, value: SecondaryValue, payer: Name)
```

## Source Code
[mi.rs](https://github.com/uuosio/rscdk/blob/main/crates/eosio-chain/src/mi.rs)
