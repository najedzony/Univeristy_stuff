process.stdin.on('data', data => {
    console.log(`Witaj ${data.toString()}`);
    process.exit();
  });