use std::env;
use std::error::Error;
use std::fs::File;
use std::io;
use std::io::prelude::*;
use std::path::Path;

fn calc(mass: i64) -> i64 {
    (((mass as f64) / 3.0).floor() as i64) - 2
}

fn part_one(lines: &std::vec::Vec<i64>) -> Result<i64, std::io::Error> {
    let mut result = 0;
    for mass in lines {
        // println!("{}", mass);
        let intermediate = calc(*mass);
        result += intermediate;
    }
    println!("{}", result);
    Ok(result)
}

fn part_two(lines: &std::vec::Vec<i64>) -> Result<i64, std::io::Error> {
    let mut result = 0;
    for mass in lines {
        // println!("{}", mass);
        let mut intermediate = calc(*mass);
        while intermediate >= 0 {
            result += intermediate;
            intermediate = calc(intermediate);
        }
    }
    println!("{}", result);
    Ok(result)
}

fn main() -> Result<(), std::io::Error> {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        panic!("Missing arg!");
    }

    let filename = &args[1];
    let _contents;
    let _lines;
    match read(filename.to_string()) {
        Err(why) => panic!("couldn't read {}: {}", filename, why.description()),
        Ok(s) => {
            // print!("{} contains:\n{}", filename, s);
            _contents = s;
        },
    }
    match read_lines(filename.to_string()) {
        Err(why) => panic!("couldn't read {}: {}", filename, why.description()),
        Ok(s) => {
            // print!("{} contains:\n{:?}", filename, s);
            _lines = s;
        },
    };
    let mut masses: Vec<i64> = Vec::new();
    for line in _lines {
        if let Ok(ip) = line {
            // println!("{}", ip);
            let mass = ip.parse::<i64>().unwrap();
            masses.push(mass);
        }
    }
    part_one(&masses)?;
    part_two(&masses)?;
    Ok(())
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines(filename: String) -> io::Result<io::Lines<io::BufReader<File>>> {
    let path = Path::new(&filename);
    let display = path.display();

    let file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why.description()),
        Ok(file) => file,
    };
    Ok(io::BufReader::new(file).lines())
}

// The output is wrapped in a Result to allow matching on errors
// Returns a String
fn read(filename: String) -> io::Result<String> {
    let path = Path::new(&filename);
    let display = path.display();

    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why.description()),
        Ok(file) => file,
    };
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why.description()),
        Ok(_) => (),
    }
    Ok(s)
}
