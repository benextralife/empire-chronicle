const fs = require('fs');
const text = fs.readFileSync('C:\\Users\\opc\\empire-chronicle\\simulator\\index.html', 'utf8');
const m = text.match(/<script[^>]*>([\s\S]*?)<\/script>/);
try {
  new Function(m[1]);
  console.log('JS syntax OK');
} catch(e) {
  // Find line number by checking each top-level construct
  const js = m[1];
  const lines = js.split('\n');
  // Try to parse line by line to find the issue
  for (let i = 0; i < lines.length; i++) {
    console.log((i+1) + ': ' + lines[i].substring(0, 100));
  }
}
