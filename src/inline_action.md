# Inline Action

An inline action initiates by contract code. Since EOS contracts does not support synchronized call to other contracts currently, inline action is the only way contracts can interact with each other.

## Code Example

```rust
#![cfg_attr(not(feature = "std"), no_std)]

#[eosio_chain::contract]
mod inline_action_example {
    use eosio_chain::{
        Name,
        action::{
            Action,
            PermissionLevel,    
        },
        name,
        ACTIVE,
        eosio_println,
    };

    #[chain(packer)]
    struct SayGoodbye {
        name: String
    }

    #[chain(main)]
    pub struct Contract {
        receiver: Name,
        first_receiver: Name,
        action: Name,
    }

    impl Contract {
        pub fn new(receiver: Name, first_receiver: Name, action: Name) -> Self {
            Self {
                receiver: receiver,
                first_receiver: first_receiver,
                action: action,
            }
        }

        #[chain(action = "sayhello")]
        pub fn say_hello(&self, name: String) {
            eosio_println!("hello", name);
            let perms: Vec<PermissionLevel> = vec![PermissionLevel{actor: name!("hello"), permission: ACTIVE}];
            let say_goodbye = SayGoodbye{name: name};
            let action = Action::new(name!("hello"), name!("saygoodbye"), &perms, &say_goodbye);
            action.send();
        }

        #[chain(action = "saygoodbye")]
        pub fn say_goodbye(&self, name: String) {
            eosio_println!("goodbye", name);
        }
    }
}
```

## Testing Code

```python
deploy_contract('inlineaction')
args = {'name': 'bob'}
r = chain.push_action('hello', 'sayhello', args)
logger.info('+++++++create elapsed: %s', r['elapsed'])
chain.produce_block()
```

The test code can be found in [examples/test.py](https://github.com/uuosio/rscdk/blob/9537fb1b9af8d3436578b937c8ab8e8255a5b9a9/examples/test.py#L202).
In this example, test code initiates a `sayhello` action with name `bob`, which prints `hello bob` to the console,
meanwhile, `sayhello` action sends `saygoodbye` action to the same contract which prints `goodbye bob` to the console.

The account needs to have an `eosio.code` permission to send an inline action. Below is the script that adds `eosio.code` permission to a contract account.

```python
def update_auth(chain, account):
    a = {
        "account": account,
        "permission": "active",
        "parent": "owner",
        "auth": {
            "threshold": 1,
            "keys": [
                {
                    "key": 'EOS6AjF6hvF7GSuSd4sCgfPKq5uWaXvGM2aQtEUCwmEHygQaqxBSV',
                    "weight": 1
                }
            ],
            "accounts": [{"permission":{"actor":account,"permission": 'eosio.code'}, "weight":1}],
            "waits": []
        }
    }
    chain.push_action('eosio', 'updateauth', a, {account:'active'})
```

## See Also
- [Action](./references/action.md)
- [Inline Action Example](https://github.com/uuosio/rscdk/tree/main/examples/inlineaction)

