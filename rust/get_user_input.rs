use std::io;

fn main()
{
	let mut user_input = String::new();
	io::stdin().read_line(&mut user_input).unwrap();
}
