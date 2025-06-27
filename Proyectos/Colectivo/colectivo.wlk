object colectivo {
    const max_pasajeros = 100 
    const max_nafta = 200
    var sense = 1 
    var nafta_actual = null
    var property gente_sobrante = false 
    var property pasajeros_subidos = null 
    var property cant_gente_sobrante = null
    var property cant_gente_a_subir = null

    method avanzar() {   

    }
    method recargar_nafta() {nafta_actual = max_nafta}
    

    method bajar_pasajeros() {
      
    }  

    method volver() {
      
    }

    method volver_urgencia() {
      
    }

    method sobra_gente() =  true

    method nafta_insuficiente() = false
}

class Ruta {
    var property parada_actual = 0 
    var property parada_sig = parada_actual + 1
    const property paradas = []
    var property cant_total_gente = 0 
    method add_paradas(cant_paradas) {
        cant_paradas.times({x => paradas.add(new Paradas(cant_minima=3, cant_maxima=10))})
    }
    method cant_paradas() = paradas.length()
    method cant_gente_in_parada() = paradas.get(parada_actual).gente()  
    method gente_total() = paradas.forEach({parada=>cant_total_gente+=parada.gente()})
}

class Paradas {
    var property cant_minima 
    var property cant_maxima
    var property cant_gente = cant_minima.randomUpTo(cant_maxima)
    method restar_pasajeros(pasajeros_a_restar) {
      cant_gente-pasajeros_a_restar
    }

}

const ruta = new Ruta()