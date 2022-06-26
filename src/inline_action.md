# Inline Action

A inline action initiates by contract code. Since EOS contract does not support synchronized call to other contracts currently, inline action is the only way contracts can interact with each other.

```rust
    let say_hello = SayHello{name: String::from("alice")};
    let perms: Vec<PermissionLevel> = vec![PermissionLevel{actor: Name::new("hello"), permission: Name::new("active")}];
    let action = Action::new(Name::new("hello"), Name::new("sayhello"), &perms, &say_hello);
    action.send();
```