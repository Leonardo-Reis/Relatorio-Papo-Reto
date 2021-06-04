session_name = document.querySelector('.session').textContent
main = document.querySelector('#main')

url = `http://192.168.0.33:5000/api/${session_name}`

const request = new XMLHttpRequest()

request.open('GET', url, false)
request.send()

lider_string = request.responseText

lider = JSON.parse(lider_string)

console.log(lider.output.membros[0])

for (membro of lider.output.membros) {
    bloco_membro = document.createElement('div')
    bloco_membro.className = 'bloco-membro'
    
    for (let semana = 0; semana < 4; semana++) {
        for (relatorio of membro.relatorios) {
            bloco_semana = document.createElement('div')
            bloco_semana.className = 'bloco-semana'
                                                                        
            h2_semana = document.createElement('h2')
            h2_semana.textContent = `Semana ${semana + 1}`
            
            contador_relatorios_nvazios = 0
            if (relatorio.semana == semana + 1  && contador_relatorios_nvazios == 0) {
                console.log("aqui")
                textarea = document.createElement('textarea')
                textarea.textContent = relatorio.relatorio
                contador_relatorios_nvazios += 1
                bloco_semana.appendChild(h2_semana)
                bloco_semana.appendChild(textarea)
            }

        }
        bloco_membro.appendChild(bloco_semana)
    }
    main.appendChild(bloco_membro)
}
