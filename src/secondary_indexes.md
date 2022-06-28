# Secondary Indexes

```rust
#![cfg_attr(not(feature = "std"), no_std)]

#[eosio_chain::contract]
mod test {

    #[chain(table="mydata")]
    pub struct MyData {
        #[chain(primary)]
        a1: u64,
        #[chain(secondary)]
        a2: u64
    }

    #[chain(contract)]
    #[allow(dead_code)]
    pub struct TestSerialzier {
        receiver: Name,
        first_receiver: Name,
        action: Name,
        value: u32,
    }

    impl TestSerialzier {

        pub fn new(receiver: Name, first_receiver: Name, action: Name) -> Self {
            Self {
                receiver: receiver,
                first_receiver: first_receiver,
                action: action,
                value: 0,
            }
        }

        #[chain(action="transfer")]
        pub fn transfer(&self, amount: Asset) -> bool {
            if self.receiver.n == 0 {
                return false;
            }
            return true;
        }


        #[chain(action="test2")]
        pub fn test2(&self) {
            let receiver = self.receiver;

            let mydb = MyData::new_mi(receiver, receiver);

            let mut it = mydb.find(1);
            if !it.is_ok() {
                //6.0
                let mydata = MyData{a1: 1, a2: 2};
                it = mydb.store(&mydata, receiver);  
            }

            let mut it = mydb.find(11);
            if !it.is_ok() {
                let mydata = MyData{a1: 11, a2: 22};
                it = mydb.store(&mydata, receiver);    
            }

            let mut it = mydb.find(111);
            if !it.is_ok() {
                let mydata = MyData{a1: 111, a2: 222};
                it = mydb.store(&mydata, receiver);
            }

            let check_fn = |it: SecondaryIterator, checker: fn(data: &MyData) -> bool | -> bool {

                let it_primary = mydb.find(it.primary);
                if !it_primary.is_ok() {
                    return false;
                }

                if let Some(x) = it_primary.get_value() {
                    if !checker(&x) {
                        return false;
                    }
                    return true;
                } else {
                    return false;
                }
            };

            //test for Idx64DB.previous
            {
                let idx = mydb.get_idx_by_a2();

                //test for Idx64DB.previous
                {
                    let it_secondary = idx.find(22 as u64);
                    let it_secondary_previous = idx.previous(it_secondary);
                    let ret = check_fn(it_secondary_previous, |data: &MyData| {
                        data.a1 == 1 && data.a2 == 2
                    });
                    check(ret, "bad secondary previous value");
                }

                //test for Idx64DB.next
                {
                    let it_secondary = idx.find(22 as u64);
                    let it_secondary_next = idx.next(it_secondary);
                    let ret = check_fn(it_secondary_next, |data: &MyData| {
                        data.a1 == 111 && data.a2 == 222
                    });
                    check(ret, "bad secondary next value");
                }

                //test for Idx64DB.lowerbound
                {
                    let (it_secondary, secondary) = idx.lowerbound(22);
                    check(it_secondary.primary == 11, "bad primary value!");
                    check(secondary == 22, "bad secondary value!");

                    let ret = check_fn(it_secondary, |data: &MyData| {
                        data.a1 == 11 && data.a2 == 22
                    });
                    check(ret, "bad secondary next value");
                }

                //test for Idx64DB.upperbound
                {
                    let (it_secondary, secondary) = idx.upperbound(22);
                    check(it_secondary.primary == 111, "upperbound: bad primary value!");
                    eosio_println!("+++++++secondary:", secondary);
                    check(secondary == 222, "upperbound: bad secondary value!");

                    let ret = check_fn(it_secondary, |data: &MyData| {
                        data.a1 == 111 && data.a2 == 222
                    });
                    check(ret, "bad secondary next value");
                }
            }
        }
    }
}
```