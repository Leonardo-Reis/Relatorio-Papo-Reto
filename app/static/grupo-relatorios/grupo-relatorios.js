const session_name = document.querySelector('.session').textContent
var main = document.querySelector('#main')

const url = `/api/${session_name}`

const request = new XMLHttpRequest()

request.open('GET', url, false)
request.send()

const lider_string = request.responseText

const lider = JSON.parse(lider_string)

console.log(lider.output.membros)
if (lider.output.membros.length != 0) {

    for (membro of lider.output.membros) {
        var bloco_membro = document.createElement('div')
        bloco_membro.className = 'bloco-membro'
    
        let h2_membro = document.createElement('h2')
        h2_membro.textContent = membro.nome
        bloco_membro.appendChild(h2_membro)
    
        let bloco_semanas = document.createElement('div')
        bloco_semanas.className = 'bloco-semanas'
    
        for (let semana = 1; semana < 5; semana++) {
            let bloco_semana = document.createElement('div')
            bloco_semana.className = 'bloco-semana'
    
            let h2_semana = document.createElement('h2')
            h2_semana.textContent = `Semana ${semana}`
            bloco_semana.appendChild(h2_semana)
    
            
            contador_relatorios_nvazios = 0
            
            for (relatorio of membro.relatorios) {
                if (relatorio.semana == semana && contador_relatorios_nvazios == 0) {
                    contador_relatorios_nvazios += 1
                    let textarea = document.createElement('textarea')
                    textarea.readOnly = true
                    textarea.textContent = relatorio.relatorio
                    
                    bloco_semana.appendChild(textarea)
                }
            }
            if (contador_relatorios_nvazios == 0) {
                let textarea = document.createElement('textarea')
                textarea.textContent = 'Sem relatorio para essa semana'
                textarea.readOnly = true
                textarea.style.color = 'red'
                textarea.style.backgroundColor = 'background-color: rgba(0,0,0,0.42);'
                
                bloco_semana.appendChild(textarea)
            }
            bloco_semanas.appendChild(bloco_semana)
            bloco_membro.appendChild(bloco_semanas)
        }
        main.appendChild(bloco_membro)
    }
} else {
    let h2_nomem = document.createElement("h1")
    h2_nomem.textContent = "Esse grupo ainda não possui membros."
    h2_nomem.style.textAlign = 'center'

    main.appendChild(h2_nomem)
}

