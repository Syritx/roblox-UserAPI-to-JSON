const { writeFile } = require("fs");

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

function GetRandomId() {
    let robloxId = Math.random()*1000000000
    console.log(robloxId)
    return Math.floor(robloxId)
}

function CreateFile(data) {
    writeFile("json_test.txt",data,(err) => {
        if (err) throw err
    })
}

function GetRequest() {
    let request = new XMLHttpRequest();

    request.open('GET', `https://games.roblox.com/v2/users/${GetRandomId()}/games?sortOrder=Asc&limit=100`)
    request.setRequestHeader('Accept', 'application/json');
    request.send();

    request.onreadystatechange = function() {
        CreateFile(request.responseText)
    }
}
GetRequest()
