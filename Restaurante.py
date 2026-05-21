# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Solución problema 2: Menú de Restaurante
# Estudiante: Johan Felipe Roncancio Guzmán

def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral):
  
    es_categoria_correcta = (categoria_producto == categoria_objetivo)
    supera_umbral_precio = (precio_base > umbral)
    
    cumple_promocion = es_categoria_correcta and supera_umbral_precio
    
    if cumple_promocion:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
        return precio_final, "SÍ"
    else:
        return precio_base, "NO"

def main():
    print("====================================================================")
    print("          SISTEMA DE PRECIOS  RESTAURANTE               ")
    print("====================================================================")
    
    menu_restaurante = [
        ["Hamburguesa Gourmet", "Comida Rápida", 25000],
        ["Papas Importadas", "Comida Rápida", 8000],
        ["Limonada Natural", "Bebidas", 7500],
        ["Jugo de Mandarina", "Bebidas", 9500],
        ["Postre tres Leches", "Postres", 12000],
        ["Helado de brownie", "Postres", 10500]
    ]
    categoria_promocion = "Bebidas"
    umbral_precio = 8000
    
    print(f"Promoción: 15% desc. en {categoria_promocion} mayores a ${umbral_precio:,}")
    print("====================================================================\n")
    
    print(f"{'PRODUCTO':<23} | {'CATEGORÍA':<15} | {'PRECIO BASE':<13} | {'¿APLICA DESC?':<13} | {'PRECIO FINAL':<13}")
    print("-" * 89)
    
    for producto in menu_restaurante:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        
        precio_final, aplica_desc = calcular_precio_final(categoria, precio_base, categoria_promocion, umbral_precio)
        
        print(f"{nombre:<23} | {categoria:<15} | ${precio_base:<12,} | {aplica_desc:<13} | ${precio_final:<12,.2f}")
        
    print("-" * 89)


if __name__ == "__main__":
    main()