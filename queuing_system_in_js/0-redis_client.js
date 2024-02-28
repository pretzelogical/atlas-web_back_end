const redis = require('redis');

async function main() {
  const client = await redis.createClient()
    .on('error', (err) => console.log('Redis client not connected to the server', err))
    .connect();

  const pong = await client.ping();

  if (pong === 'PONG') {
    console.log('Redis client connected to the server');
  } else {
    console.log('Redis client not connected to the server')
  }

  await client.disconnect();
}

main();
