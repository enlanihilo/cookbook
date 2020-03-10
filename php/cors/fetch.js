fetch('http://localhost:7777/', 
		{ headers: {'Content-Type':'text/plain'} }
	)
    .then(res => res.text() )
	.then(console.log);
