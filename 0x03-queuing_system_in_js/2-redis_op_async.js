import redis from 'redis'
import util from 'util'


const client = redis.createClient()
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`))
client.on('connect', ()=> console.log('Redis client connected to the server'))

const get = util.promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        redis.print(err, reply)
    })
}

async function displaySchoolValue(schoolName) {
    let name = await get(schoolName)
    console.log(name);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
