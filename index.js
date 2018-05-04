const Api = require('./api');

if (!process.env.DEVICE_IP) {
  console.log('Please set the IP address of your Sony audio device like this: DEVICE_IP=192.168.X.X node index.js');
  process.exit();
}

const api = new Api(`http://${process.env.DEVICE_IP}:54480/sony`);

var vol = process.ARGV[2];
api.setVolume(vol);
