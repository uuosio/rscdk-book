#![cfg_attr(not(feature = "std"), no_std)]

#[eosio_chain::contract]
mod mi_example {
    use eosio_chain::{
        Name,
        name,
        eosio_println,
    };

    #[derive(Default)]
    pub struct MyData1 {
        key: u64,
        count: u64,
    }

    impl ::eosio_chain::serializer::Packer for MyData1 {
        fn size(&self) -> usize {
            let mut _size: usize = 0;
            _size += self.key.size();
            _size += self.count.size();
            return _size;
        }
        fn pack(&self) -> Vec<u8> {
            let mut enc = ::eosio_chain::serializer::Encoder::new(self.size());
            enc.pack::<u64>(&self.key);
            enc.pack::<u64>(&self.count);
            return enc.get_bytes();
        }
        fn unpack(&mut self, data: &[u8]) -> usize {
            let mut dec = ::eosio_chain::serializer::Decoder::new(data);
            dec.unpack::<u64>(&mut self.key);
            dec.unpack::<u64>(&mut self.count);
            return dec.get_pos();
        }
    }

    impl ::eosio_chain::db::PrimaryValueInterface for MyData1 {
        fn get_primary(&self) -> u64 {
            return self.key.to_primary_value();
        }
    }

    impl ::eosio_chain::db::SecondaryValueInterface for MyData1 {
        #[allow(unused_variables, unused_mut)]
        fn get_secondary_value(&self, i: usize) -> eosio_chain::db::SecondaryValue {
            return eosio_chain::db::SecondaryValue::None;
        }

        #[allow(unused_variables, unused_mut)]
        fn set_secondary_value(&mut self, i: usize, value: eosio_chain::db::SecondaryValue) {}
    }

    #[chain(main)]
    #[allow(dead_code)]
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

        #[chain(action = "inc")]
        pub fn inc_count(&self) {
            let indexes: [eosio_chain::db::SecondaryType; 0usize] = [];

            #[allow(dead_code)]
            fn unpacker(data: &[u8]) -> MyData1 {
                let mut ret = MyData1::default();
                ret.unpack(data);
                return ret;
            }
            let code = self.receiver;
            let scope = Name::from_u64(0);
            let mi = eosio_chain::mi::MultiIndex::new(code, scope, name!("mydata1"), &indexes, unpacker);
            let it = mi.find(1);

            let ram_payer = self.receiver;
            if let Some(mut value) = it.get_value() {
                value.count += 1;
                mi.update(&it, &value, ram_payer);
                eosio_println!("++++++count:", value.count);
            } else {
                let value = MyData1{
                    key: 1,
                    count: 1,
                };
                mi.store(&value, ram_payer);
                eosio_println!("++++++count:", value.count);
            }
        }
    }
}
