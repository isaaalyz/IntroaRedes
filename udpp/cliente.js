const dgram = require('dgram');
const readline = require('readline');

const client = dgram.createSocket('udp4');
const PORT = 9000;
const HOST = 'localhost';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter your name: ', (name) => {
    function promptMessage() {
        rl.question('Type your message: ', (msg) => {
            const bodyMessage = `${name}!=${msg}`;
            client.send(bodyMessage, PORT, HOST, (err) => {
                if (err) console.error(err);
                promptMessage();
            });
        });
    }
    promptMessage();
});
