use std::io::{self, Write};

fn bruteforce_hash(hash: &str) -> String {
    for a in 32..128 {
        for b in 32..128 {
            for c in 32..128 {
                if format!("{:x}", md5::compute([a, b, c])) == hash {
                    return String::from_utf8([a, b, c].to_vec()).unwrap();
                }
            }
        }
    }
    panic!("Not found!");
}

fn main() {
    let hashes: [u64; 18] = [
        0xFE5D3A093968D02B,
        0xBA0AA367C2862EAE,
        0x8BEA2ADA9E26604F,
        0x2E6F41C96DCF5224,
        0x7FD91BD2949B75F3,
        0x5B1ED8E6072F3A6,
        0xC94045C6D4887611,
        0x9D43DF6DF6B94D95,
        0xB9A8A83C8AC08D80,
        0x6D78E80376518464,
        0xE81A20F2023C2D0,
        0x2E41EAE69D89F186,
        0x425C831DD2A3E5FD,
        0x82788DBBDC4100EC,
        0x6D0FEE8D3901DD20,
        0xEBE82A0A41E5D783,
        0x2AFA26414B72E506,
        0xD1848E9C21D114D,
    ];

    for h in hashes.chunks(2) {
        let mut t = String::new();
        for x in h {
            for c in x.to_le_bytes() {
                t += format!("{:02x}", c).as_str();
            }
        }
        print!("{}", bruteforce_hash(&t));
        let _ = io::stdout().flush();
    }
}
