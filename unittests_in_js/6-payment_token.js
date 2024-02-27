async function getPaymentTokenFromAPI(success) {
  const testFunc = async () => {
    return { 'data': 'Successful response from the API' };
  }
  if (success) {
    return await testFunc();
  }
}

module.exports = getPaymentTokenFromAPI;
