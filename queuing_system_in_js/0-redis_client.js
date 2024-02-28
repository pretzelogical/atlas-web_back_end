import { createClient } from 'redis';

async function main() {
  const client = await createClient().connect();

  console.log(client);

  const pong = await client.ping();

  if (pong === 'PONG') {
    console.log('Redis client connected to the server');
  } else {
    console.log('Redis client not connected to the server')
  }

  await client.disconnect();
}

main();
