const dgram = require('dgram');
const server = dgram.createSocket('udp4');

const PORT = 9000;
const HOST = 'localhost';

server.on('listening', () => {
    console.log(`Servidor UDP iniciado em ${HOST}:${PORT}`);
});

server.on('message', (msg, rinfo) => {
    const message = msg.toString();
    const [name, content] = message.split('!=');
    console.log(`[${name.toUpperCase()}]: ${content}`);
});

server.bind(PORT, HOST);
