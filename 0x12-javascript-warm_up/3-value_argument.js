// #!/usr/bin/node

// script that prints the first argument passed to it:
// If no arguments are passed to the script, print “No argument”
// You must use console.log(...) to print all output

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
}

if (args.length > 0) {
  console.log(args[0]);
}
