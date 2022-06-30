# Action

## new

```rust
pub fn new(account: Name, name: Name, authorization: &Vec<PermissionLevel>, data: &dyn Packer) -> Self
```

Creates an action by specifying contract account, action name, authorization and data.

## send

```rust
pub fn send(&self)
```

Send inline action to contract.
