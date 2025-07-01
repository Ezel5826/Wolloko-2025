
class Poligono {
    const property segmento1 = 3
    const property segmento2 = 5
    const property segmento3 = 6

    method es_equilatero() = segmento1==segmento2 and segmento2==segmento3 
    
    method es_isosceles() = segmento1==segmento2 or segmento1==segmento3 and segmento1!=segmento2 or segmento1!=segmento3 

    method es_escaleno() = segmento1!=segmento2 and segmento2!=segmento3 
}