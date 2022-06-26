# DBI64

## struct DBI64

```rust
pub struct DBI64<T>
where T: Packer + PrimaryValueInterface + Default,
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

## new

```rust
pub fn new(code: Name, scope: Name, table: Name) -> Self
```

Creates a new DBI64 instance

## store

```rust
pub fn store(&self, key: u64,  value: &T, payer: Name) -> Iterator<T>
```

Store a value indexes by `key`. `payer` specifies account to pay the RAM resources.
VM throws an exception which can't catch by contract code if there is already a value with `key` exists in the database.

The following example code shows how to check if a value with the `key` already exists.

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


## find

```rust
pub fn find(&self, key: u64) -> Iterator<T>
```

Find value by primary key


## update

```rust
pub fn update(&self, iterator: &Iterator<T>, value: &T, payer: u64)
```

Update a value in database.
`payer` specifies account to pay the RAM resources. 
The related action in transaction must contain a corresponding permission of `payer`.

## remove

```rust
pub fn remove(&self, iterator: &Iterator<T>)
```

Remove value from database by iterator

## get

```rust
pub fn get(&self, iterator: &Iterator<T>) -> Option<T>
```

Get value by iterator. use `Iterator::get_value()` method for a more convenient way.

## next
```rust
pub fn next(&self, iterator: &Iterator<T>) -> Iterator<T>
```

Get next iterator

## previous

```rust
pub fn previous(&self, iterator: &Iterator<T>) -> Iterator<T>
```

Get previous iterator

## lowerbound

```rust
pub fn lowerbound(&self, key: u64) -> Iterator<T>
```

Return a iterator with a key >= `key`

## upperbound

```rust
pub fn upperbound(&self, key: u64) -> Iterator<T>
```

Return a iterator with a key > `key`

## end

```rust
pub fn end(&self) -> Iterator<T>
```

Return an end iterator, Iterator.is_end() return true if it's a valid end iterator.
This method is often used with `previous` method to get the last iterator.

```rust
let mut it = db.end();
if it.is_end() {
    it = db.previous();
    //...
}
```
