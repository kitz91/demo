const btoa = require('btoa');
const atob = require('atob');

//verify test value after passing demo proxy is base 64 encoded
function isBase64(image) {
	try {
        return (btoa(atob(image)) == image);
    } catch (err) {
        return false;
    }
}


//verify the encoded value is in fact test
function isTest(image) {
	try {
        return {result:((atob(image)) == "test"), string:(atob(image))};
    } catch (err) {
        return {result:0, string:""};
    }}


module.exports = {isBase64, isTest};