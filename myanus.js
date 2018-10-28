
var ws281x = require('rpi-ws281x-native');


/**
* Setup
*/
var NUM_LEDS = 150,
    pixelData = new Uint32Array(NUM_LEDS);

ws281x.init(NUM_LEDS);

// ---- trap the SIGINT and reset before exit
process.on('SIGINT', function () {
  ws281x.reset();
  process.nextTick(function () { process.exit(0); });
});




//for(var i = 0; i < NUM_LEDS; i++) {
//    pixelData[i] = 0xff0000;
//}
//ws281x.render(pixelData);

// ---- animation-loop
//var t0 = Date.now();
//setInterval(function () {
//    var dt = Date.now() - t0;
//
//    ws281x.setBrightness(
//        Math.floor(Math.sin(dt/250) * 128 + 128));
//}, 1000 / 30);

console.log('Press <ctrl>+C to exit.');

colorWipe(ws281x, pixelData, 0xff0000);

function colorWipe(strip, pixelData, color) {
    for(var i = 0; i < NUM_LEDS; i++) {
        pixelData[i] = 0xff0000;
        strip.render(pixelData);
    }
}