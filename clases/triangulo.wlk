class Segmentos {
    const property longitud 
}

object poligono {
    const property segmento1 = new Segmentos(longitud=4)
    const property segmento2 = new Segmentos(longitud=4)
    const property segmento3 = new Segmentos(longitud=4)

    method es_equilatero() = segmento1.longitud()==segmento2.longitud() and segmento2.longitud()==segmento3.longitud() 
    
    method es_isosceles() = segmento1.longitud()==segmento2.longitud() or segmento1.longitud()==segmento3.longitud() and segmento1.longitud()!=segmento2.longitud() or segmento1.longitud()!=segmento3.longitud() 

    method es_escaleno() = segmento1.longitud()!=segmento2.longitud() and segmento2.longitud()!=segmento3.longitud() 
}