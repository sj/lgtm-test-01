
function helloWorld(message){
	console.log("Hello World! Here's a message: " + message);
}

// lgtm.com should catch this alert:
helloWorld('hope lgtm.com finds this alert', 'some extra trailing argument that should be flagged up');

// lgtm.com should suppress this alert:
helloWorld('hope lgtm.com finds this alert', 'some extra trailing argument that should be flagged up'); // lgtm [js/superfluous-trailing-arguments]
