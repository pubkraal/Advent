use structopt::StructOpt;

mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;
mod day07;
mod day08;

#[derive(StructOpt)]
struct Cli {
    #[structopt(default_value="all")]
    day: String,
}

fn main() {
    let args = Cli::from_args();

    let day: i32;
    let thing = args.day.parse::<i32>();
    match thing {
        Ok(n) => day = n,
        Err(_) => day = 0,
    }

    match day {
        1 => day01::run(),
        2 => day02::run(),
        3 => day03::run(),
        4 => day04::run(),
        5 => day05::run(),
        6 => day06::run(),
        7 => day07::run(),
        8 => day08::run(),
        _ => (),
    }
    if args.day == "all" {
        day01::run();
        day02::run();
        day03::run();
        day04::run();
        day05::run();
        day06::run();
        day07::run();
        day08::run();
    }
}
