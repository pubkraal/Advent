use structopt::StructOpt;

mod day01;
mod day02;
mod day03;

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
        _ => (),
    }
    if args.day == "all" {
        day01::run();
        day02::run();
        day03::run();
    }
}
