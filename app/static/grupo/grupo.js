session_name = document.querySelector('.session').textContent

url = `http://192.168.0.33:5000/api/${session_name}`

const request = new XMLHttpRequest()

request.open('GET', url, false)
request.send()

lider_string = request.responseText

lider = JSON.parse(lider_string)

for (membro of lider.output.membros) {
    console.log(membro)
}
