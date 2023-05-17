function round(value, decimals) {
    return Number(Math.round(value + 'e' + decimals) + 'e-' + decimals).toFixed(decimals);
}

function calc() {
    let capital = document.getElementById('value');
    let tempo = document.getElementById('time');
    let taxa = document.getElementById('tax');
    let filler = document.getElementById('filler');
    let montante = 0;

    capital = parseInt(capital.value);
    tempo = parseInt(tempo.value);
    taxa = parseInt(taxa.value);
    taxa /= 100;
    
    let calc1 = (1+taxa)**tempo;
    let calc2 = calc1*capital;
    montante = calc2;

    let parcela_med = parseFloat(montante.toFixed(2));
    filler.innerHTML = 'A parcela mensal média tem valor = R$' + parcela_med;
}

function clean() {
    filler.innerHTML = '';
    document.getElementById('formy').reset();
}