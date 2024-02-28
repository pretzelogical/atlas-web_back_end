const redis = require('redis');

function getClient() {
  const client = redis.createClient();
  client.on('error', (err) => console.log('Redis client not connected to the server', err));
  return client.connect().then(() => client).catch(err => console.error(err));
}

function setNewSchool(schoolName, value) {
  getClient().then(client => {
    client.set(schoolName, value)
      .then(res => {
        console.log(`Reply: ${res}`);
        client.disconnect();
      })
      .catch(err => console.error(err));
  }).catch(err => console.error(err));
}

function displaySchoolValue(schoolName) {
  getClient().then(client => {
    client.get(schoolName)
      .then(res => {
        console.log(res);
        client.disconnect();
      })
      .catch(err => console.error(err));
  }).catch(err => console.error(err));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
